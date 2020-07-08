from flask import jsonify
from marshmallow import ValidationError

from . import main


@main.app_errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err), 400