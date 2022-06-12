from port import db


class Permission:

    id = db.Column(db.Integer, primary_key=True)


class UserPermission:

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    permission_id = db.Column(db.Integer, db.ForeignKey('Permission.id'))
