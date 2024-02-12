from flask import request, jsonify
from datetime import datetime
from app.models.visitor import Visitor
from app.extensions import db
from app.visitor import bp
from app import helper


# Create a new visitor
@bp.route('/', methods=['POST'])
@helper.token_required
def create_visitor(current_manager):
    data = request.json
    new_visitor = Visitor(influencer_id=data['influencer_id'], referer=data.get('referer'), location=data.get('location'),
                          link_id=data['link_id'], headers=data.get('headers', {}), created_at=datetime.utcnow())
    db.session.add(new_visitor)
    db.session.commit()
    return jsonify({"message": "Visitor created successfully."}), 201

# Retrieve all visitors
@bp.route('/', methods=['GET'])
@helper.token_required
def get_visitors(current_manager):
    visitors = Visitor.query.all()
    visitors_data = [{"visitor_id": visitor.visitor_id, "influencer_id": visitor.influencer_id,
                      "referer": visitor.referer, "location": visitor.location,
                      "link_id": visitor.link_id, "created_at": visitor.created_at,
                      "headers": visitor.headers} for visitor in visitors]
    return jsonify(visitors_data)

# Retrieve a specific visitor
@bp.route('/<int:visitor_id>', methods=['GET'])
@helper.token_required
def get_visitor(current_manager, visitor_id):
    visitor = Visitor.query.get_or_404(visitor_id)
    visitor_data = {"visitor_id": visitor.visitor_id, "influencer_id": visitor.influencer_id,
                    "referer": visitor.referer, "location": visitor.location,
                    "link_id": visitor.link_id, "created_at": visitor.created_at,
                    "headers": visitor.headers}
    return jsonify(visitor_data)

# Update an existing visitor
@bp.route('/<int:visitor_id>', methods=['PUT'])
@helper.token_required
def update_visitor(current_manager, visitor_id):
    visitor = Visitor.query.get_or_404(visitor_id)
    data = request.json
    visitor.referer = data.get('referer', visitor.referer)
    visitor.location = data.get('location', visitor.location)
    visitor.headers = data.get('headers', visitor.headers)
    db.session.commit()
    return jsonify({"message": "Visitor updated successfully."})

# Delete a visitor
@bp.route('/<int:visitor_id>', methods=['DELETE'])
@helper.token_required
def delete_visitor(current_manager, visitor_id):
    visitor = Visitor.query.get_or_404(visitor_id)
    db.session.delete(visitor)
    db.session.commit()
    return jsonify({"message": "Visitor deleted successfully."})
