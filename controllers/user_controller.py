from flask import Blueprint, request, jsonify
from models.user import User
from services.user_service import UserService
from sqlalchemy.exc import SQLAlchemyError

user_blueprint = Blueprint('user_blueprint', __name__)
user_service = UserService()  # Assuming you have a UserService for business logic

@user_blueprint.route('/users', methods=['GET'])
def get_users():
    try:
        users = user_service.get_all_users()
        return jsonify([user.to_dict() for user in users]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@user_blueprint.route('/user', methods=['POST'])
def create_user():
    try:
        user_data = request.json
        user = user_service.create_user(user_data)
        return jsonify(user.to_dict()), 201
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@user_blueprint.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        user_data = request.json
        updated_user = user_service.update_user(user_id, user_data)
        return jsonify(updated_user.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@user_blueprint.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        user_service.delete_user(user_id)
        return jsonify({'message': 'User deleted successfully'}), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

