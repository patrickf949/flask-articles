from flask import Blueprint, make_response, jsonify, request
from app.models import Users

client = Users()

user = Blueprint('user', __name__)

@user.route('/')
def welcome():
    return "Welcome! Karibu!"

@user.route('/auth/register', methods=['POST'])
def create_user():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    confirm_password = request.json['confirm_password']

    
    if not client.validate_email(email):
        return jsonify(
            {'error': 'email should be in the form someone@example.com', 'status': 400}), 400
    if not client.valid_password(password):
        return jsonify(
            {'error': 'password should be atleast 6 characters, \
                uppercase letters of the alphabet, numbers and cannot have empty spaces', 'status': 400}), 400
    if not client.valid_username(username):
        return jsonify(
            {'error': 'username field should have length of atleast 3 characters, \
            should not have empty spaces, cannot be empty and should contain alphabets', 'status': 400}), 
    if client.confirm_password(password, confirm_password):
        return jsonify(
            {'error': 'Passwords do not match!', 'status': 400}), 400
    check_user = client.check_username(username)
    if check_user:
        return jsonify({'message': 'username already exist', 'status': 400}), 400
    check_email = client.check_email(email)
    if check_email:
        return jsonify({'message': 'email already exists', 'status': 400}), 400

    signup_data = {
        "username": username,
        "email": email,
        "password": password,
        "confirm_password": confirm_password
    }
    client.register_user(signup_data)
    return make_response(jsonify({"message": "User registered successfully", "status": 201}), 201)
