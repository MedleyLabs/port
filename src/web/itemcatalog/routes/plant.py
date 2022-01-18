from flask import (render_template, url_for, request,
                   redirect, Blueprint, abort, flash)

from itemcatalog import db
from itemcatalog.models.plant import Plant

plant = Blueprint('plant', __name__)


@plant.route("/plant/create", methods=['GET', 'POST'])
def create_plant():
    """ CREATE Plant """

    print('CREATE plant...')

    r = request.data

    print('Request data:', r)

    new_plant = Plant(name=r.name,
                      days_between_water=r.days_between_water,
                      days_between_fertilizer=r.days_between_fertilizer,
                      days_between_repot=r.days_between_repot)

    db.session.add(new_plant)
    db.session.commit()

    print('Success!')

    return 'Success!'
