import json
import pytz

from datetime import datetime
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

timezone = pytz.timezone('US/Mountain')


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


@plant.route("/plant/today", methods=['GET'])
def get_today():
    """ Returns the plant care scheduled to be done today """

    print('Running GET /plant/today...')

    status_fertilize = get_fertilize_status().json
    status_repot = get_repot_status().json
    status_water = get_water_status().json

    status_fertilize = [s[:2] + 'Fertilize - ' + s[2:] for s in status_fertilize]
    status_repot = [s[:2] + 'Repot - ' + s[2:] for s in status_repot]
    status_water = [s[:2] + 'Water - ' + s[2:] for s in status_water]

    status_all = (status_fertilize + status_repot + status_water)
    status_all = [status for status in status_all if '🟢' not in status]
    status_all.sort()

    return jsonify(status_all)


@plant.route("/plant/status", methods=['GET'])
def get_status():
    """ Checks the status of water, repot, and fertilizer """

    def extract_highest_status(status_names):
        """ Finds the highest priority status from a list of statuses """

        combined = '\t'.join(status_names)

        if '🔴' in combined:
            return '🔴'
        if '🟡' in combined:
            return '🟡'
        if '🟢' in combined:
            return '🟢'

    water_status = get_water_status().json
    repot_status = get_repot_status().json
    fertilize_status = get_fertilize_status().json

    status = [
        f'{extract_highest_status(water_status)} Water plants',
        f'{extract_highest_status(fertilize_status)} Fertilize plants',
        f'{extract_highest_status(repot_status)} Repot plants',
    ]

    response = jsonify(status)

    return response


@plant.route("/plant/status/fertilize", methods=['GET'])
def get_fertilize_status():
    """ Returns a status emoji (green/yellow/red circle) plus its name """

    print('Running GET /plant/status/fertilize...')

    plants = Plant.query.filter(Plant.is_active).all()

    status_names = []

    for p in plants:

        entries = FertilizeEntry.query.filter(FertilizeEntry.plant_id == p.id) \
                                      .order_by(FertilizeEntry.created_at.desc()) \
                                      .all()

        current_date = datetime.now(timezone).date()

        if entries:
            last_date = entries[-1].created_at.date()
            date_delta = (current_date-last_date).days
        else:
            created_date = p.created_at.date()
            date_delta = (current_date-created_date).days

        if date_delta > p.days_between_fertilize:
            status_emoji = '🔴'
        elif date_delta == p.days_between_fertilize:
            status_emoji = '🟡'
        else:
            status_emoji = '🟢'

        status_name = f'{status_emoji} {p.name}'
        status_names.append(status_name)

    response = jsonify(status_names)
    print(response.data)

    return response


@plant.route("/plant/status/repot", methods=['GET'])
def get_repot_status():
    """ Returns a status emoji (green/yellow/red circle) plus its name """

    print('Running GET /plant/status/repot...')

    plants = Plant.query.filter(Plant.is_active).all()

    status_names = []

    for p in plants:

        entries = RepotEntry.query.filter(RepotEntry.plant_id == p.id) \
                                  .order_by(RepotEntry.created_at.desc()) \
                                  .all()

        current_date = datetime.now(timezone).date()

        if entries:
            last_date = entries[-1].created_at.date()
            date_delta = (current_date-last_date).days
        else:
            created_date = p.created_at.date()
            date_delta = (current_date-created_date).days

        if date_delta > p.days_between_repot:
            status_emoji = '🔴'
        elif date_delta == p.days_between_repot:
            status_emoji = '🟡'
        else:
            status_emoji = '🟢'

        status_name = f'{status_emoji} {p.name}'
        status_names.append(status_name)

    response = jsonify(status_names)

    return response


@plant.route("/plant/status/water", methods=['GET'])
def get_water_status():
    """ Returns a status emoji (green/yellow/red circle) plus its name """

    print('Running GET /plant/status/water...')

    plants = Plant.query.filter(Plant.is_active).all()

    status_names = []

    for p in plants:

        entries = WaterEntry.query.filter(WaterEntry.plant_id == p.id) \
                                  .order_by(WaterEntry.created_at.desc()) \
                                  .all()

        current_date = datetime.now(timezone).date()

        if entries:
            last_date = entries[-1].created_at.date()
            date_delta = (current_date-last_date).days
        else:
            created_date = p.created_at.date()
            date_delta = (current_date-created_date).days

        if date_delta > p.days_between_water:
            status_emoji = '🔴'
        elif date_delta == p.days_between_water:
            status_emoji = '🟡'
        else:
            status_emoji = '🟢'

        status_name = f'{status_emoji} {p.name}'
        status_names.append(status_name)

    response = jsonify(status_names)

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
        days_between_fertilize=r['days_between_fertilize'],
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

    for key, value in r['updates'].items():
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

        name = name[2:]

        plant_id = Plant.query.filter(Plant.name == name).first().to_dict()['id']

        entry = WaterEntry(
            plant_id=plant_id,
            created_at=r['datetime'],
        )

        db.session.add(entry)
        db.session.commit()

    return jsonify({"status_code": 200})
