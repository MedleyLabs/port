from flask import (
    Blueprint,
    jsonify,
    request,
)

from itemcatalog import db
from itemcatalog.models.plant import Plant

plant = Blueprint('plant', __name__)


@plant.route("/plant", methods=['GET'])
def get_plant():
    """ """

    print('Running /plant...')

    plants = Plant.query.all()
    plants = [p.as_dict() for p in plants]
    response = jsonify(plants)

    print('/plant response:', response.__dict__)

    return response


@plant.route("/plant/name", methods=['GET'])
def get_plant_name():
    """ """

    print('Running /plant/name...')

    plants = Plant.query.all()
    plants = [p.as_dict()['name'] for p in plants]
    response = jsonify(plants)

    print('/plant/name response:', response.__dict__)

    return response


@plant.route("/plant/create", methods=['GET', 'POST'])
def create_plant():
    """ Creates a new plant """

    print('Running /plant/create...')

    r = request.get_json()

    print('Request data:', r)

    new_plant = Plant(name=r['name'],
                      days_between_water=r['days_between_water'],
                      days_between_fertilizer=r['days_between_fertilizer'],
                      days_between_repot=r['days_between_repot'])

    db.session.add(new_plant)
    db.session.commit()

    print(f'''Added plant with name "{r['name']}"!''')

    return 'Success!'
