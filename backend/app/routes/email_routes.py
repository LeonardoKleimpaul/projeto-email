from flask import Blueprint, jsonify, request
from app.models.email import Email

email_bp = Blueprint('email', __name__)

@email_bp.route('/hello')
def hello():
    return jsonify({'message': 'Email route funcionando!'})

@email_bp.route('/', methods=['GET'])
def index():
    emails = Email.query.all()
    return jsonify([email.to_dict() for email in emails])

@email_bp.route('/new', methods=['POST', 'OPTIONS'])
def create_email():
    if request.method == 'OPTIONS':
        return '', 200

    email_data = request.get_json()
    email = Email(**email_data)
    email.save()
    return jsonify(email.to_dict()), 201

@email_bp.route('/edit/<int:email_id>', methods=['PUT'])
def edit_email(email_id):
    email_data = request.get_json()
    email = Email.query.get(email_id)
    if not email:
        return jsonify({'error': 'Email não encontrado'}), 404
    for key, value in email_data.items():
        setattr(email, key, value)
    email.save()
    return jsonify(email.to_dict())

@email_bp.route('/delete/<int:email_id>', methods=['DELETE'])
def delete_email(email_id):
    email = Email.query.get(email_id)
    if not email:
        return jsonify({'error': 'Email não encontrado'}), 404
    email.delete()
    return jsonify({'message': 'Email deletado com sucesso'})
