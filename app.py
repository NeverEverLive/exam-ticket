from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from src.models.base import set_session
from settings.config import settings


def create_app():
    app = Flask(__name__, root_path='')
    app.config["SQLALCHEMY_DATABASE_URI"] = settings.DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= settings.SQLALCHEMY_TRACK_MODIFICATIONS

    set_session()

    return app


if __name__ == "__main__":
    app = create_app()
    from src.views.api import api
    app.register_blueprint(api)
    app.run(debug=True, port=5001)

# @app.route('/')
# def test():
#     return 'test'
