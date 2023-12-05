from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from OOP_DEV.config import DevelopmentConfig

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    from OOP_DEV.controllers.user_controller import user_blueprint
    app.register_blueprint(user_blueprint)

    return app
