from flask import Flask
from .database import Database
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import app_config

db = db = SQLAlchemy()

def create_app(config_type = 'production'):
    ap = Flask(__name__)
    Bootstrap(ap)
    ap.config['SECRET_KEY'] = 'Alimanuakokoroapac'
    ap.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://sammy:bOllo972398kladlfFao@localhost:5432/sammy'
    ap.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(ap)
    ap.config.from_object(app_config[config_type])
    # Database()
    from app.views.user_views import user
    from app.views.article_views import article
    ap.register_blueprint(user)
    ap.register_blueprint(article)

    return ap


