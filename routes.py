from flask import request, jsonify, abort, Blueprint
from models import db, Message


chat_bp = Blueprint("chat", __name__, url_prefix='/chat')
@chat_bp.route('/', methods=['POST'])
def get_response():
    data = request.json
    if not data or 'content' not in data or "user_id" not in data:
        abort(400, description="content and user_id are mandatory")
    content = data['content']
    user_id = data['user_id']
    new_message = Message(content=content, user_id=user_id)
    db.session.add(new_message)
    db.session.commit()
    response = "dosmth and itll be fixed"
    new_message.fillResponse(response)
    db.session.commit()
    return jsonify(new_message.toJson())


messages_bp = Blueprint("messages", __name__, url_prefix='/messages')
@messages_bp.route('/', methods=['GET'])
def get_messages():
    messages = Message.query.all()
    return jsonify([ m.toJson() for m in messages])

@messages_bp.route('/', methods=['POST'])
def create_message():
    data = request.json
    if not data or 'content' not in data or "user_id" not in data:
        abort(400, description="content and user_id are mandatory")
    new_message = Message(user_id=data['user_id'], content=data['content'])
    db.session.add(new_message)
    db.session.commit()
    return jsonify(new_message.toJson()), 201

@messages_bp.route('/<int:message_id>', methods=['PUT'])
def update_message(message_id):
    data = request.json
    message = Message.query.get_or_404(message_id)
    message.content = data['content']
    db.session.commit()
    return jsonify(message.toJson())

@messages_bp.route('/<int:message_id>', methods=['DELETE'])
def delete_message(message_id):
    message = Message.query.get_or_404(message_id)
    db.session.delete(message)
    db.session.commit()
    return jsonify({"message": "Deleted successfully"})
