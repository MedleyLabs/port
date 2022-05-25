from port import app, db
from port.models.base_model import BaseModel

from .exceptions import PaymentError


class GasolinePurchase(BaseModel):
    """ A single purchase of gasoline from a source """

    __tablename__ = 'gasoline_purchase'

    id = db.Column(db.Integer, primary_key=True)
    number_of_gallons = db.Column(db.Float, nullable=False)
    number_of_miles_driven = db.Column(db.Float)
    octane = db.Column(db.Integer)
    total_cost = db.Column(db.Float)
    purchase_date = db.Column(db.DateTime())

    @property
    def dollars_per_gallon(self):
        """ The price that would be displayed on the gas station sign """
        return self.total_cost / self.number_of_gallons if self.total_cost else None

    @property
    def miles_per_gallon(self):
        """ The fuel efficiency of the vehicle """
        return self.number_of_miles_driven / self.number_of_gallons if self.number_of_miles_driven else None


class CarbonEmission(BaseModel):
    """ An amount of carbon emitted from burning gasoline """

    __tablename__ = 'carbon_emission'

    pounds_gasoline_per_gallon = 6.3
    carbon_atomic_weight = 12
    oxygen_atomic_weight = 16
    co2_atomic_weight = carbon_atomic_weight + 2 * oxygen_atomic_weight
    co2_to_carbon_weight_ratio = co2_atomic_weight / carbon_atomic_weight

    id = db.Column(db.Integer, primary_key=True)
    pounds_co2 = db.Column(db.Float, nullable=False)
    gasoline_purchase_id = db.Column(db.Integer, db.ForeignKey('gasoline_purchase.id'))

    @classmethod
    def create(cls, number_of_gallons, octane=87, gasoline_purchase_id=None):

        pounds_carbon_per_gallon = cls.pounds_gasoline_per_gallon * octane
        pounds_co2_per_gallon = pounds_carbon_per_gallon * cls.co2_to_carbon_weight_ratio
        pounds_co2 = pounds_co2_per_gallon * number_of_gallons

        obj = cls(pounds_co2=pounds_co2, gasoline_purchase_id=gasoline_purchase_id)
        db.session.add(obj)
        db.session.commit()

        return obj


class CarbonOffset(BaseModel):

    dollars_per_ton_co2 = 50  # TODO Make it so this can vary over time
    pounds_per_ton = 2000

    @classmethod
    def create(cls, pounds_co2, carbon_emission_id=None):

        total_cost = pounds_co2/cls.pounds_per_ton * cls.dollars_per_ton_co2

        try:
            cls.send_payment(total_cost)
        except PaymentError as e:
            print(e)

        obj = cls(pounds_co2=pounds_co2, total_cost=total_cost, carbon_emission_id=carbon_emission_id)
        db.session.add(obj)
        db.session.commit()

        cls.send_payment(total_cost)

        return obj

    @classmethod
    def send_payment(cls, total_cost, destination='The Carbon Offset Company'):
        print(f'Sent ${total_cost} to {destination}...')






