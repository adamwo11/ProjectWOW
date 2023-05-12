from flask import Blueprint
from controllers.char_controllers import index, new, create

char_routes = Blueprint('char_routes', __name__)


char_routes.route('')(index)

char_routes.route('/generate')(new)

char_routes.route('/generate', methods=['GET'])(create)
