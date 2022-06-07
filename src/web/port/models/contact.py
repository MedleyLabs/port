from port import db


class Email:

    id = db.column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    address = db.Column(db.String, nullable=False)


class Phone:

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    country_code = db.Column(db.String, nullable=False)
    ten_digit_number = db.Column(db.String, nullable=False)


class SocialAccount:

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    platform = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)