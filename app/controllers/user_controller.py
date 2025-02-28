from flask import Blueprint, request, jsonify
from app.models.user import create_user, get_user_by_email
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token
from app.models.user import get_user_by_email

bcrypt = Bcrypt()

def signup():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if not name or not email or not password:
        return jsonify({'message': 'Missing required fields'}), 400

    existing_user = get_user_by_email(email)

    if existing_user:
        return jsonify({'message': 'User already exists'}), 400

    password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    create_user(name, email, password_hash)

    return jsonify({'message': 'User created successfully'}), 201

def signin():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Missing required fields'}), 400

    user = get_user_by_email(email)

    if user and bcrypt.check_password_hash(user[3], password):
        access_token = create_access_token(identity=str(user[0]))
        return jsonify({'access_token': access_token}), 200

    return jsonify({'message': 'Invalid credentials'}), 401