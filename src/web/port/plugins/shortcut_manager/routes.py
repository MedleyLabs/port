from flask import (
    Blueprint,
    jsonify,
    request,
)

from server import db
from server.models.shortcut import (
    Shortcut,
    ShortcutDependencies,
)

shortcut = Blueprint('shortcut', __name__)


@shortcut.route("/shortcut", methods=['GET'])
def get_shortcuts():
    """ """

    print('Running /shortcut...')

    shortcuts = Shortcut.query.all()
    shortcuts = [p.to_dict() for p in shortcuts]

    response = jsonify(shortcuts)

    print('/shortcut response:', response)

    return response


@shortcut.route("/shortcut/name", methods=['GET'])
def get_shortcut_names():
    """ """

    print('Running GET /shortcut/name...')

    shortcuts = Shortcut.query.all()
    shortcuts = [p.to_dict()['name'] for p in shortcuts]
    response = jsonify(shortcuts)

    print('/shortcut/name response:', response)

    return response


@shortcut.route("/shortcut/create", methods=['POST'])
def create_shortcut():
    """ Creates a new shortcut """

    print('Running /shortcut/create...')

    r = request.get_json()

    print('Request data:', r)

    new_shortcut = Shortcut(**r)

    db.session.add(new_shortcut)
    db.session.commit()

    print(f'''Added shortcut with name "{r['name']}"!''')

    return jsonify({"status_code": 200})


@shortcut.route("/shortcut/update", methods=['POST'])
def update_shortcut():
    """ """

    print(f'Running POST /shortcut/update...')

    r = request.get_json()

    print('Request data:', r)

    shortcut_obj = Shortcut.query.filter(Shortcut.name == r['name']).first()
    response = jsonify(shortcut_obj)

    print('/shortcut/name response:', response.__dict__)

    return response
