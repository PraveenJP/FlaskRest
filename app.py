import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

from models import Result, User, users_schema, user_schema

@app.route('/')
def get_tasks():
    return jsonify('Flask Restful API')

# endpoint to create new user
@app.route('/user', methods=["POST"])
def add_user():
    username = request.json['username']
    email = request.json['email']
    new_user = User(username, email)
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify('Success')
    except Exception as e:
        return jsonify(e)

# endpoint to show all users
@app.route('/user', methods=["GET"])
def get_user():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result.data)

# endpoint to get user detail by id
@app.route('/user/<id>', methods=["GET"])
def user_detail(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)

# endpoint to update user
@app.route('/user/<id>', methods=["PUT"])
def user_update(id):
    user = User.query.get(id)
    username = request.json['username']
    email = request.json['email']
    user.email = email
    user.username = username
    db.session.commit()
    return user_schema.jsonify(user)

# endpoint to delete user
@app.route('/user/<id>', methods=["DELETE"])
def user_delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return user_schema.jsonify(user)

if __name__ == '__main__':
    app.run(debug=True)

