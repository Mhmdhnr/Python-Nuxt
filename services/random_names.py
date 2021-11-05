from flask_restful import Resource, reqparse
from business.random_names import get_random_name


class RandomNames(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('count', type=int, required=True,
                        help='This field cannot be left blank')

    def get(self, count):
        return [name.json() for name in get_random_name(count)]



