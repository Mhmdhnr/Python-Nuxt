from db import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(80), nullable=True)
    email_address = db.Column(db.String(80), nullable=True)
    username = db.Column(db.String(80), nullable=True)
    password = db.Column(db.String(80), nullable=True)
    first_name = db.Column(db.String(80), nullable=True)
    last_name = db.Column(db.String(80), nullable=True)

    def __init__(self, user_id=None, phone_number=None, user_name=None, password=None, email_address=None, first_name=None, last_name=None):
        self.id = user_id
        self.phone_number = phone_number
        self.username = user_name
        self.password = password
        self.email_address = email_address
        self.first_name = first_name
        self.last_name = last_name


    def json(self):
        return {
            'user_id': self.id,
            'phone_number': self.phone_number,
            'email_address': self.email_address,
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def is_authenticated(self):
        return True


class Token(db.Model):
    __tablename__ = 'Tokens'

    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(80), nullable=False)
    token = db.Column(db.String(80), nullable=False)
    expiration_date_time = db.Column(db.DateTime)

    def __init__(self, phone_number, token, expiration_date_time):
        self.phone_number = phone_number
        self.token = token
        self.expiration_date_time = expiration_date_time

    def json(self):
        return {'id': self.id,
                'phone_number': self.phone_number,
                'token': self.token,
                'expiration_date_time': self.expiration_date_time}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

