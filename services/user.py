from flask_restful import Resource, reqparse
from business.user import sign_in_up, send_token, sign_out


class SignInUp(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('phone_number', type=str, required=False,
                        help='')
    parser.add_argument('token', type=str, required=False,
                        help='')
    parser.add_argument('username', type=str, required=False,
                        help='')
    parser.add_argument('password', type=str, required=False,
                        help='')

    def post(self):
        data = SignInUp.parser.parse_args()
        result = sign_in_up(data['phone_number'], data['token'], data['username'], data['password'])
        return result


class Token(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('phone_number', type=str, required=True,
                        help='')

    def post(self):
        data = Token.parser.parse_args()
        return send_token(data['phone_number'])


class SignOut(Resource):
    def get(self):
        return sign_out()
