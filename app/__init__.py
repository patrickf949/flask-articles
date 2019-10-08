from flask import Flask
from .database import Database


def create_app():
    ap = Flask(__name__)
    Database()
    from app.views.user_views import user
    ap.register_blueprint(user)

    return ap