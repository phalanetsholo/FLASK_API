from flask import Blueprint
from app.controllers.user_controller import signup, signin

user_bp = Blueprint('user', __name__)

user_bp.route('/signup', methods=['POST'])(signup)
user_bp.route('/signin', methods=['POST'])(signin)