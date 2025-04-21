from flask import Blueprint, jsonify
from app.models.email import Email

email_bp = Blueprint('email', __name__)

@email_bp.route('/hello')
def hello():
    return jsonify({'message': 'Email route funcionando!'})
