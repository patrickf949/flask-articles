from flask import Blueprint
user = Blueprint('user', __name__)

@user.route('/')
def welcome():
    return "Welcome to Karibu!"