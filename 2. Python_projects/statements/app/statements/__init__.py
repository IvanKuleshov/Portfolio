# -*- coding: utf-8 -*-
# app/journal/__init__.py

from flask import Blueprint

statements = Blueprint('statements', __name__, template_folder='templates', static_folder='static')

from . import views
