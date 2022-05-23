from flask import (
    Blueprint,
    jsonify,
    request,
)

from server import db
from server.models.substance import (
    Entry,
    Route,
    Substance,
    SubstanceRoute
)


substance = Blueprint('substance', __name__)


@substance.route("/substance", methods=['GET'])
def get_substances():
    """ """

    print('Running GET /substance...')

    substances = Substance.query.all()
    substances = [s.to_dict() for s in substances]
    response = jsonify(substances)

    print('/substance response:', response.__dict__)

    return response


@substance.route("/substance/create", methods=['POST'])
def create_substance():
    """ Creates a new substance """

    print('Running POST /substance/create...')

    r = request.get_json()
    print('Request data:', r)

    route = r['route']

    valid_routes = get_routes()

    if route in valid_routes:
        pass

    new_entry = Substance(
        amount=r['amount'],
        created_at=r['created_at']
    )

    db.session.add(new_entry)
    db.session.commit()

    print(f'''Added substance with name "{r['name']}"!''')

    return jsonify({"status_code": 200})


@substance.route("/substance/entry/create", methods=['POST'])
def create_entry():
    """ Creates a new entry for a substance """

    print('Running POST /substance/entry...')

    r = request.get_json()
    print('Request data:', r)

    substance_id = ...

    new_entry = Entry(
        substance_id=substance_id,
        amount=r['amount'],
        created_at=r['created_at']
    )

    db.session.add(new_entry)
    db.session.commit()

    print(f'''Added entry with substance name "{r['name']}"!''')

    return jsonify({"status_code": 200})


@substance.route("/substance/route", methods=['POST'])
def get_routes():
    """ """

    print('Running GET /route...')

    substances = SubstanceRoute.query.all()
    substances = [s.to_dict() for s in substances]
    response = jsonify(substances)

    print('/substance response:', response.__dict__)

    return response

@substance.route("/substance/route/create", methods=['POST'])
def create_route():
    """ Creates a new route for a substance. """

    print('Running POST /substance/route/create...')

    r = request.get_json()
    print('Request data:', r)

    new_entry = SubstanceRoute(
        name=r['name'],
        units=r['units']
    )

    db.session.add(new_entry)
    db.session.commit()

    print(f'''Added entry with route name "{r['name']}"!''')

    return jsonify({"status_code": 200})
