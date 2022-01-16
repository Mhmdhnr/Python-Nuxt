from models.user import User, Token
from models.user_test_results import UserTestResults
from business.otp import send_verification_token
from datetime import datetime
from flask_login import login_user, logout_user, current_user


def sign_in_up(phone_number=None, token=None, username=None, password=None):
    if None not in (phone_number, token):
        db_token = Token.query.filter_by(phone_number=phone_number).first()
        print(db_token.expiration_date_time)
        print(datetime.now())
        print(db_token.token)
        if db_token.token == token and db_token.expiration_date_time > datetime.now():
            user = User.query.filter_by(phone_number=phone_number).first()
            if user:
                login_user(user)
                return {'message': "Successfully signed in"}
            else:
                new_user = User(phone_number)
                new_user.save_to_db()
                login_user(user)
                return {'message': "Successfully signed up"}
        elif db_token.token != token and db_token.expiration_date_time > datetime.now():
            return "wrong token"
        elif db_token.token == token and db_token.expiration_date_time < datetime.now():
            return {'message': "Token expired"}
        else:
            return {'message': "Wrong token and expired"}


def sign_out():
    logout_user()
    return {'message': 'Signed Out'}, 201


def send_token(phone_number):
    return send_verification_token(phone_number)
