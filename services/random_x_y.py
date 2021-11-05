from flask_restful import Resource, reqparse
from business.random_x_y import get_x_y


class RandomXY(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('count', type=int, required=True,
                        help='This field cannot be left blank')

    def get(self, count):
        return [x_y.json() for x_y in get_x_y(count)]



