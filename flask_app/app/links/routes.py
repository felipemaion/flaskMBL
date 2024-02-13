from app.links import bp
from app.extensions import db
from flask import jsonify, request
from app.models.link import Link
import hashlib
from app import helper

@bp.route("/", methods=["POST"])
@helper.token_required
@helper.manager_required
def create_link(current_manager):
    data = request.json
    if "url_reduced" in data and data["url_reduced"]:  # If url_reduced is provided
        existing_link = Link.query.filter_by(url_reduced=data["url_reduced"]).first()
        if existing_link:
            return jsonify({"error": "Provided url_reduced is already in use."}), 400
        else:
            new_link = Link(
                link_name=data["link_name"],
                url=data["url"],
                url_reduced=data["url_reduced"],
                isvisible=data.get("isvisible", True),
                influencer_id=data["influencer_id"],
            )
    else:
        hash_value = hashlib.sha256(
            data["url"].encode()
            + data["link_name"].encode()
            + str(data["influencer_id"]).encode()
        ).hexdigest()[:8]
        new_link = Link(
            link_name=data["link_name"],
            url=data["url"],
            url_reduced=hash_value,
            isvisible=data.get("isvisible", True),
            influencer_id=data["influencer_id"],
        )
    db.session.add(new_link)
    db.session.commit()
    return (jsonify({
                "message": "Link created successfully.",
                "url_reduced": new_link.url_reduced,
            }), 201,)

@bp.route("/", methods=["GET"])
@helper.token_required
@helper.manager_required
def get_links(current_manager):
    links = Link.query.all()
    links_data = [
        {
            "link_id": link.link_id,
            "link_name": link.link_name,
            "url": link.url,
            "url_reduced": link.url_reduced,
            "isvisible": link.isvisible,
            "influencer_id": link.influencer_id,
            "created_at": link.created_at,
        }
        for link in links
    ]
    return jsonify(links_data)

@bp.route("/<int:link_id>", methods=["GET"])
@helper.token_required
@helper.manager_required
def get_link(current_manager, link_id):
    link = Link.query.get_or_404(link_id)
    link_data = {
        "link_id": link.link_id,
        "link_name": link.link_name,
        "url": link.url,
        "url_reduced": link.url_reduced,
        "isvisible": link.isvisible,
        "influencer_id": link.influencer_id,
        "created_at": link.created_at,
    }
    return jsonify(link_data)

@bp.route("//<int:link_id>", methods=["PUT"])
@helper.token_required
@helper.manager_required
def update_link(current_manager, link_id):
    link = Link.query.get_or_404(link_id)
    data = request.json
    link.link_name = data["link_name"]
    link.url = data["url"]
    link.url_reduced = data["url_reduced"]
    link.isvisible = data["isvisible"]
    link.influencer_id = data["influencer_id"]
    db.session.commit()
    return jsonify({"message": "Link updated successfully."})

@bp.route("/<int:link_id>", methods=["DELETE"])
@helper.token_required
@helper.manager_required
def delete_link(current_manager, link_id):
    link = Link.query.get_or_404(link_id)
    db.session.delete(link)
    db.session.commit()
    return jsonify({"message": "Link deleted successfully."})
