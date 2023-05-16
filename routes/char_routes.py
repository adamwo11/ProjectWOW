from flask import Blueprint
from controllers.char_controllers import index, new, create, character, edit, update, delete, like

char_routes = Blueprint('char_routes', __name__)


char_routes.route('')(index)

char_routes.route('/generate')(new)

char_routes.route('/generate', methods=['GET'])(create)

char_routes.route('/new_char', methods=['GET'])(character)

char_routes.route('/<id>/edit')(edit)

char_routes.route('/<id>', methods=["POST"])(update)

char_routes.route('/<id>/delete', methods=["POST"])(delete)

char_routes.route('/<id>/likes', methods=["POST"])(like)