from . import main
from marshmallow import ValidationError

@main.app_errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err), 400