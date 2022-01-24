from flask import (
    Blueprint,
    jsonify,
    request,
)

from itemcatalog import db
from itemcatalog.models.plant import (
    Plant,
    FertilizeEntry,
    RepotEntry,
    WaterEntry,
)

plant = Blueprint('plant', __name__)


@plant.route("/plant", methods=['GET'])
def get_plants():
    """ """

    print('Running GET /plant...')

    plants = Plant.query.all()
    plants = [p.to_dict() for p in plants]
    response = jsonify(plants)

    print('/plant response:', response.__dict__)

    return response


@plant.route("/plant/name", methods=['GET'])
def get_plant_names():
    """ """

    print('Running GET /plant/name...')

    plants = Plant.query.filter(Plant.is_active).all()
    plants = [p.to_dict()['name'] for p in plants]
    response = jsonify(plants)

    print('/plant/name response:', response.__dict__)

    return response


@plant.route("/plant/create", methods=['POST'])
def create_plant():
    """ Creates a new plant """

    print('Running POST /plant/create...')

    r = request.get_json()

    print('Request data:', r)

    new_plant = Plant(
        name=r['name'],
        days_between_water=r['days_between_water'],
        days_between_fertilizer=r['days_between_fertilizer'],
        days_between_repot=r['days_between_repot'],
        created_at=r['created_at']
    )

    db.session.add(new_plant)
    db.session.commit()

    print(f'''Added plant with name "{r['name']}"!''')

    return jsonify({"status_code": 200})


@plant.route("/plant/update", methods=['POST'])
def update_plant():
    """ """

    print(f'Running POST /plant/update...')

    r = request.get_json()

    print('Request data:', r)

    p = Plant.query.filter(Plant.name == r['name']).first()

    for key, value in r['updates'].keys():
        setattr(p, key, value)

    db.session.commit()

    return jsonify({"status_code": 200})


@plant.route("/plant/delete", methods=['POST'])
def delete_plants():
    """ Note that this unchecks the is_active field, not deleting the row """

    print('Running POST /plant/delete...')

    r = request.get_json()

    print('Request data:', r)

    plant_names = r['plant_names']

    if type(plant_names) is str:
        plant_names = [plant_names]

    for name in plant_names:
        p = Plant.query.filter(Plant.name == name).first()
        p.is_active = False

        db.session.commit()

    return jsonify({"status_code": 200})


@plant.route("/plant/fertilize", methods=['POST'])
def create_fertilize_entry():
    """ Records the plant being fertilized """

    print('Running POST /plant/fertilize...')

    r = request.get_json()

    print('Request data:', r)

    plant_names = r['plant_names']

    if type(plant_names) is str:
        plant_names = [plant_names]

    for name in plant_names:

        plant_id = Plant.query.filter(Plant.name == name).first().to_dict()['id']

        entry = FertilizeEntry(
            plant_id=plant_id,
            created_at=r['datetime'],
        )

        db.session.add(entry)
        db.session.commit()

    return jsonify({"status_code": 200})


@plant.route("/plant/repot", methods=['POST'])
def create_repot_entry():
    """ Records the plant being repotted """

    print('Running POST /plant/repot...')

    r = request.get_json()

    print('Request data:', r)

    plant_names = r['plant_names']

    if type(plant_names) is str:
        plant_names = [plant_names]

    for name in plant_names:

        plant_id = Plant.query.filter(Plant.name == name).first().to_dict()['id']

        entry = RepotEntry(
            plant_id=plant_id,
            created_at=r['datetime'],
        )

        db.session.add(entry)
        db.session.commit()

    return jsonify({"status_code": 200})


@plant.route("/plant/water", methods=['POST'])
def create_water_entry():
    """ Records the plant being watered """

    print('Running POST /plant/water...')

    r = request.get_json()

    print('Request data:', r)

    plant_names = r['plant_names']

    if type(plant_names) is str:
        plant_names = [plant_names]

    for name in plant_names:

        plant_id = Plant.query.filter(Plant.name == name).first().to_dict()['id']

        entry = WaterEntry(
            plant_id=plant_id,
            created_at=r['datetime'],
        )

        db.session.add(entry)
        db.session.commit()

    return jsonify({"status_code": 200})
