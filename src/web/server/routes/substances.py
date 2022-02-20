import pytz

from datetime import datetime, timedelta
from flask import (
    Blueprint,
    jsonify,
    request,
)

from server import db
from server.models.substances import Entry


substances = Blueprint('substance', __name__)


@substances.route("/substances/create", methods=['POST'])
def create_plant():
    """ Creates a new plant """

    print('Running POST /substance/create...')

    r = request.get_json()

    print('Request data:', r)

    new_plant = Entry(
        name=r['name'],
        dose_quantity=r['dose'],
        dose_units=r['dose_units'],
        created_at=r['created_at']
    )

    db.session.add(new_plant)
    db.session.commit()

    print(f'''Added substance with name "{r['name']}"!''')

    return jsonify({"status_code": 200})