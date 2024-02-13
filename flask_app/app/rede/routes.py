from app.rede import bp
from app.extensions import db
from flask import jsonify, request
from app.models.rede import Rede
from app import helper

@bp.route("/", methods=["POST"])
@helper.token_required
@helper.admin_required
def create_rede(current_manager):
    data = request.json
    new_rede = Rede(rede_id=data["rede_id"], name=data["name"])
    db.session.add(new_rede)
    db.session.commit()
    return jsonify({"message": "Rede created successfully."}), 201


@bp.route("/", methods=["GET"])
@helper.token_required
@helper.manager_required
def get_rede(current_manager):
    redes = Rede.query.all()
    rede_data = [
        {
            "rede_id": rede.rede_id,
            "name": rede.name,
        }
        for rede in redes
    ]
    return jsonify(rede_data)


@bp.route("/<int:rede_id>", methods=["GET"])
@helper.token_required
@helper.manager_required
def get_rede_by_id(current_manager,rede_id):
    # print(rede_id)
    rede = Rede.query.get_or_404(rede_id)
    rede_data = {"rede_id": rede.rede_id, "name": rede.name}
    return jsonify(rede_data)


@bp.route("/<int:rede_id>", methods=["PUT"])
@helper.token_required
@helper.admin_required
def update_rede(current_rede, rede_id):
    rede = Rede.query.get_or_404(rede_id)
    data = request.json
    rede.name = data["name"]
    db.session.commit()
    return jsonify({"message": "Rede updated successfully."})


@bp.route("/<int:rede_id>", methods=["DELETE"])
@helper.token_required
@helper.admin_required
def delete_rede(current_rede, rede_id):
    rede = Rede.query.get_or_404(rede_id)
    db.session.delete(rede)
    db.session.commit()
    return jsonify({"message": "Rede deleted successfully."})
