from app.manager import bp
from app.extensions import db
from flask import jsonify, request
from app.models.manager import Manager

@bp.route('/', methods=['POST'])
def create_manager():
    data = request.json
    new_manager = Manager(user_name=data['user_name'], password=data['password'])
    db.session.add(new_manager)
    db.session.commit()
    return jsonify({"message": "Manager created successfully."}), 201

@bp.route('/', methods=['GET'])
def get_managers():
    managers = Manager.query.all()
    managers_data = [{"manager_id": manager.manager_id, "user_name": manager.user_name} for manager in managers]
    return jsonify(managers_data)

@bp.route('/<int:manager_id>', methods=['GET'])
def get_manager(manager_id):
    manager = Manager.query.get_or_404(manager_id)
    manager_data = {"manager_id": manager.manager_id, "user_name": manager.user_name}
    return jsonify(manager_data)

@bp.route('/<int:manager_id>', methods=['PUT'])
def update_manager(manager_id):
    manager = Manager.query.get_or_404(manager_id)
    data = request.json
    manager.user_name = data['user_name']
    manager.password = data['password']
    db.session.commit()
    return jsonify({"message": "Manager updated successfully."})

@bp.route('/<int:manager_id>', methods=['DELETE'])
def delete_manager(manager_id):
    manager = Manager.query.get_or_404(manager_id)
    db.session.delete(manager)
    db.session.commit()
    return jsonify({"message": "Manager deleted successfully."})
