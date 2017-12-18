"""
    Details: User Controller
    Author: praveenjp
"""
from flask import request, jsonify
from app.user.models import User, users_schema, user_schema
from app import app, db


@app.route('/')
def get_tasks():
    """
    :return: Sample Test
    """
    return jsonify('Flask Restful API')


@app.route('/user', methods=["POST"])
def add_user():
    """
    :param: Username and email
    :return: Success or failer based on insert data
    """
    username = request.json['username']
    email = request.json['email']
    new_user = User(username, email)
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify('Success')
    except Exception as e:
        return jsonify(e)


@app.route('/user', methods=["GET"])
def get_user():
    """
    :return: Get all the user data
    """
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result.data)


@app.route('/user/<id>', methods=["GET"])
def user_detail(id):
    """
    :param id: User ID
    :return: User data
    """
    user = User.query.get(id)
    return user_schema.jsonify(user)


@app.route('/user/<id>', methods=["PUT"])
def user_update(id):
    """
    :param id: User ID
    :return: Updated user result
    """
    user = User.query.get(id)
    username = request.json['username']
    email = request.json['email']
    user.email = email
    user.username = username
    db.session.commit()
    return user_schema.jsonify(user)


@app.route('/user/<id>', methods=["DELETE"])
def user_delete(id):
    """
    :param id: User ID
    :return: Deleted user Result
    """
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return user_schema.jsonify(user)
