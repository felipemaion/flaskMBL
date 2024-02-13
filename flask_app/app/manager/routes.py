from app.manager import bp
from app.extensions import db
from flask import jsonify, request
from app.models.manager import Manager, Role
from app import helper

@bp.route("/", methods=["POST"])
@helper.token_required
@helper.admin_required
def create_manager(current_manager):
    data = request.json
    new_manager = Manager(user_name=data["user_name"], password=data["password"], role=Role[data["role"]])
    db.session.add(new_manager)
    db.session.commit()
    return jsonify({"message": "Manager created successfully."}), 201

@bp.route("/", methods=["GET"])
@helper.token_required
@helper.manager_required
def get_managers(current_manager):
    managers = Manager.query.all()
    managers_data = [
        {
            "manager_id": manager.manager_id,
            "user_name": manager.user_name,
            "password": manager.password,
            "role":str(manager.role),
        } for manager in managers
    ]
    return jsonify(managers_data)

@bp.route("/<int:manager_id>", methods=["GET"])
@helper.token_required
@helper.manager_required
def get_manager(current_manager,manager_id):
    manager = Manager.query.get_or_404(manager_id)
    manager_data = {"manager_id": manager.manager_id, "user_name": manager.user_name, "role":manager.role}
    return jsonify(manager_data)

@bp.route("/<int:manager_id>", methods=["PUT"])
@helper.token_required
@helper.admin_required
def update_manager(current_manager, manager_id):
    manager = Manager.query.get_or_404(manager_id)
    data = request.json
    manager.user_name = data["user_name"].strip() if data["user_name"].strip() else manager.user_name
    manager.password = data["password"].strip() if data["password"].strip() else manager.password
    manager.role = Role[data["role"].strip()] if data["role"].strip() else manager.role
    db.session.commit()
    return jsonify({"message": "Manager updated successfully."})

@bp.route("/<int:manager_id>", methods=["DELETE"])
@helper.token_required
@helper.admin_required
def delete_manager(current_manager, manager_id):
    manager = Manager.query.get_or_404(manager_id)
    db.session.delete(manager)
    db.session.commit()
    return jsonify({"message": "Manager deleted successfully."})
