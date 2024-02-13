from app.influencer import bp
from app.extensions import db
from app.models.influencer import Influencer
from flask import jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.exceptions import BadRequest
from app import helper

@bp.route('/')
@helper.token_required
@helper.manager_required
def get_influencers(current_manager):
    influencers_list = Influencer.query.all()
    return jsonify([{"influencer_id": influencer.influencer_id, "name": influencer.name,"url":f"mblink/{influencer.url}"} for influencer in influencers_list])

@bp.route('/', methods=['POST'])
@helper.token_required
@helper.admin_required
def create_influencer(current_manager):
    data = request.get_json()
    try:
        if not data or 'name' not in data or 'url' not in data:  # Basic validation to check if name exists
            raise BadRequest('Missing fields in request data')
        new_influencer = Influencer(name=data['name'],url=data['url'])
        db.session.add(new_influencer)
        db.session.commit()
        return jsonify({"message": "Influencer created successfully", "influencer_id": new_influencer.influencer_id}), 201
    except SQLAlchemyError as e:
        db.session.rollback()  # Rollback the session to a clean state
        return jsonify({"DB error": str(e)}), 500
    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred."}), 500

@bp.route('/<int:influencer_id>', methods=['PUT'])
@helper.token_required
@helper.admin_required
def update_influencer(current_manager, influencer_id):
    data = request.get_json()
    try:
        influencer = Influencer.query.get_or_404(influencer_id)
        influencer.name = data.get('name', influencer.name)
        db.session.commit()
        return jsonify({"message": "Influencer updated successfully", "influencer_id": influencer.influencer_id})
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"DB error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred."}), 500
    
@bp.route('/influencers/<int:influencer_id>', methods=['DELETE'])
@helper.token_required
@helper.admin_required
def delete_influencer(current_manager, influencer_id):
        influencer = Influencer.query.get_or_404(influencer_id)
        db.session.delete(influencer)
        db.session.commit()
        return jsonify({"message": "Influencer deleted successfully"}), 500