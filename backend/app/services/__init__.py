from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from .config import Config

db=SQLAlchemy()
jwt=JWTManager()

def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)

    from .routes.auth import auth_bp
    from .routes.workouts import workout_bp

    app.register_blueprint(auth_bp,url_prefix='/auth')
    app.register_blueprint(workout_bp,url_prefix='/workouts')
    return app

