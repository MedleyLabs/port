from flask import (
    Blueprint,
    jsonify,
    request,
)

from itemcatalog import db
from itemcatalog.models.plant import Plant

plant = Blueprint('plant', __name__)


@plant.route("/plant", methods=['GET'])
def get_plants():
    """ """

    plants = Plant.query.all()
    response = jsonify([p.as_dict() for p in plants])

    return response


@plant.route("/plant/create", methods=['GET', 'POST'])
def create_plant():
    """ Creates a new plant """

    print('CREATE plant...')

    r = request.get_json()

    print('Request data:', r)

    new_plant = Plant(name=r['name'],
                      days_between_water=r['days_between_water'],
                      days_between_fertilizer=r['days_between_fertilizer'],
                      days_between_repot=r['days_between_repot'])

    db.session.add(new_plant)
    db.session.commit()

    print('Success!')

    return 'Success!'
