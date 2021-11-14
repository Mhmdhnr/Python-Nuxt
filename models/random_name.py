from db import db


class RandomNames:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def json(self):
        return {'first_name': self.first_name,
                'last_name': self.last_name}


class PersianFirstName(db.Model):
    __tablename__ = 'PersianFirstName'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    gender = db.Column(db.Boolean)

    def __init__(self, first_name, gender):
        self.first_name = first_name
        self.gender = gender

    def json(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'gender': self.gender,
        }


class PersianLastName(db.Model):
    __tablename__ = 'PersianLastName'

    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(80))

    def __init__(self, last_name):
        self.last_name = last_name

    def json(self):
        return {
            'id': self.id,
            'last_name': self.last_name,
        }


