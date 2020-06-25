from flask import jsonify

def expired_token_callback():
    return jsonify({
        "description": "The token has expired.",
        "error": "token_expired"
    }), 401

def invalid_token_callback(error):
    return jsonify({
        "description": "Signature verification failed.",
        "error": "invalid_token"
    }), 401

def missing_token_callback(error):
    return jsonify({
        "description": "Request does not contain an access token.",
        "error": "authorization_required"
    }), 401

def token_not_fresh_callback():
    return jsonify({
        "description": "The token is not fresh.",
        "error": "fresh_token_required"
    }), 401

def revoked_token_callback():
    return jsonify({
        "description": "The token has been revoked.",
        "error": "token_revoked"
    }), 401