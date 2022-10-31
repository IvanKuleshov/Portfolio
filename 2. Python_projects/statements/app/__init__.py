# -*- coding: utf-8 -*-
# app/__init__.py

from pathlib import Path
from flask import Flask
from .extensions import db
from .statements import statements


def create_app():
    app = Flask(__name__, static_folder='/statements/static/', static_url_path ='/statements/static/')
    app.config["SECRET_KEY"] = 'SECRET_KEY'
    cwd = Path(__file__).parent.parent
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{str(cwd.joinpath('statements.db'))}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    app.register_blueprint(statements)
    return app
