import pytz

from datetime import datetime
from flask import (
    Blueprint,
    jsonify,
    request,
)

from . import config
from .models import (
    CarbonEmission,
    CarbonOffset,
    GasolinePurchase
)

carbon_offset = Blueprint('carbon_offset', __name__)

timezone = pytz.timezone('US/Mountain')

default_gasoline_type = config['default_gasoline_type']


@carbon_offset.route('/carbon_offset/gasoline_purchase', methods=['POST'])
def gasoline_purchase():
    """ """

    print('POST /carbon_offset/gasoline_purchase...')

    data = request.get_json()

    number_of_gallons = data.get('number_of_gallons')
    number_of_miles_driven = data.get('number_of_miles_driven')
    type_of_gasoline = data.get('type_of_gasoline', default_gasoline_type)
    total_cost = data.get('total_cost')
    purchase_date = data.get('purchase_date', datetime.now())

    purchase = GasolinePurchase.create(
        number_of_gallons=number_of_gallons,
        number_of_miles_driven=number_of_miles_driven,
        type_of_gasoline=type_of_gasoline,
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

    return ''

