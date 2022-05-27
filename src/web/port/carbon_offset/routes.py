import pytz

from datetime import datetime
from flask import (
    Blueprint,
    jsonify,
    request,
)

from .config import config
from .models import (
    CarbonEmission,
    CarbonOffset,
    GasolinePurchase
)

db.drop_all()
db.create_all()

carbon_offset = Blueprint('carbon_offset', __name__)

default_octane = config['default_octane']


@carbon_offset.route('/carbon_offset/gasoline_purchase', methods=['POST'])
def gasoline_purchase():
    """ """

    print('POST /carbon_offset/gasoline_purchase...')

    data = request.get_json()

    number_of_gallons = data.get('number_of_gallons')
    number_of_miles_driven = data.get('number_of_miles_driven')
    octane = data.get('octane', default_octane)
    total_cost = data.get('total_cost')
    purchase_date = data.get('purchase_date', datetime.now())

    purchase = GasolinePurchase.create(
        number_of_gallons=number_of_gallons,
        number_of_miles_driven=number_of_miles_driven,
        octane=octane,
        total_cost=total_cost,
        purchase_date=purchase_date
    )

    emission = CarbonEmission.create(
        number_of_gallons=number_of_gallons,
        gasoline_purchase_id=purchase.id
    )

    offset = CarbonOffset.create(
        pounds_co2=emission.pounds_co2,
        carbon_emission_id=emission.id
    )

    print(f'Finished! offset.id={offset.id}')

    return f'Your purchase created {emission.pounds_co2} pounds of CO2!'

