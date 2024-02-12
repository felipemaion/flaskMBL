from app.links import bp
from app.links import bp
from app.extensions import db
from flask import jsonify, request
from app.models.link import Link
import hashlib

## LINKS
# Create a new link
@bp.route('/', methods=['POST'])
def create_link():
    data = request.json
    if 'url_reduced' in data and data['url_reduced']:  # If url_reduced is provided
        existing_link = Link.query.filter_by(url_reduced=data['url_reduced']).first()
        if existing_link:
            return jsonify({"error": "Provided url_reduced is already in use."}), 400
        else:
            new_link = Link(link_name=data['link_name'], url=data['url'], url_reduced=data['url_reduced'],
                            isvisible=data.get('isvisible', True), influencer_id=data['influencer_id'])
    else:  # If url_reduced is not provided, generate a reduced link using hash
        hash_value = hashlib.sha256(data['url'].encode() + data['link_name'].encode()+ str(data['influencer_id']).encode()).hexdigest()[:8]  # Using hash for simplicity
        new_link = Link(link_name=data['link_name'], url=data['url'], url_reduced=hash_value,
                        isvisible=data.get('isvisible', True), influencer_id=data['influencer_id'])
    
    db.session.add(new_link)
    db.session.commit()
    return jsonify({"message": "Link created successfully.", "url_reduced": new_link.url_reduced}), 201

# Retrieve all links
@bp.route('/', methods=['GET'])
def get_links():
    links = Link.query.all()
    links_data = [{"link_id": link.link_id, "link_name": link.link_name, "url": link.url,
                   "url_reduced": link.url_reduced, "isvisible": link.isvisible,
                   "influencer_id": link.influencer_id, "created_at": link.created_at} for link in links]
    return jsonify(links_data)

# Retrieve a specific link
@bp.route('/<int:link_id>', methods=['GET'])
def get_link(link_id):
    link = Link.query.get_or_404(link_id)
    link_data = {"link_id": link.link_id, "link_name": link.link_name, "url": link.url,
                 "url_reduced": link.url_reduced, "isvisible": link.isvisible,
                 "influencer_id": link.influencer_id, "created_at": link.created_at}
    return jsonify(link_data)

# Update an existing link
@bp.route('//<int:link_id>', methods=['PUT'])
def update_link(link_id):
    link = Link.query.get_or_404(link_id)
    data = request.json
    link.link_name = data['link_name']
    link.url = data['url']
    link.url_reduced = data['url_reduced']
    link.isvisible = data['isvisible']
    link.influencer_id = data['influencer_id']
    db.session.commit()
    return jsonify({"message": "Link updated successfully."})

# Delete a link
@bp.route('/<int:link_id>', methods=['DELETE'])
def delete_link(link_id):
    link = Link.query.get_or_404(link_id)
    db.session.delete(link)
    db.session.commit()
    return jsonify({"message": "Link deleted successfully."})