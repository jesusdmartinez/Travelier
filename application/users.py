from flask import Blueprint, jsonify, request, render_template
from . import db
from .models import User

NewUsersApi = Blueprint('new_users', __name__)

@NewUsersApi.route('/', methods=['POST'])
def create_user():
    try:
        new_user = User.create_user(request.json)
    except KeyError as e:
        return jsonify(f'Missing key: {e.args[0]}'), 400
    db.session.add(new_user)
    db.session.commit()
    return jsonify(), 200


@NewUsersApi.route('<first_name>', methods=['GET'])
def get_user(first_name):
    username = User.query.filter(User.first_name == first_name).first()
    if username is None:
        return 'user not found', 404
    return jsonify(username.retrieve_users()), 200