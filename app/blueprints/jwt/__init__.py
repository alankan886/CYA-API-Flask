from flask import Blueprint

jwt = Blueprint('jwt_bp', __name__)

from . import loaders