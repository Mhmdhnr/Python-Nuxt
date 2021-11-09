from flask_restful import Resource, reqparse
from models.tests import Tests

class Tests(Resource):
    # parser = reqparse.RequestParser()
    # parser.add_argument('count', type=int, required=True,
    #                     help='This field cannot be left blank')

    def get(self):
        return [test.json() for test in Tests.query.all()]



