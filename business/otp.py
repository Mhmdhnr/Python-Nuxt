import random
from kavenegar import *
from datetime import datetime, timedelta
from models.user import Token
# import jdatetime

api = KavenegarAPI('742B515534747831364233325255505043744F534C513D3D')


class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)


def send_verification_token(phone_number):
    token = random.randint(1111, 9999)
    print(phone_number)
    params = {'sender': '10000010101101', 'receptor': phone_number, 'message': f"کد احراز هویت شما " + "\n" + f"{token}"}
    response = api.sms_send(params)
    obj = Struct(**response[0])
    send_time = datetime.utcfromtimestamp(obj.date)
    print(send_time)
    expiration_time = send_time + timedelta(minutes=20)
    print(expiration_time)
    to_insert = Token(phone_number, token, expiration_time)
    if not Token.query.filter_by(phone_number=phone_number).first():
        to_insert.save_to_db()
    else:
        Token.delete_from_db(Token.query.filter_by(phone_number=phone_number).first())
        to_insert.save_to_db()
    return response

