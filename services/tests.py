from flask_restful import Resource, reqparse
from models.tests import Test, Question, Choice
from business.tests import calculate_raven_result


class TestsServices(Resource):
    # parser = reqparse.RequestParser()
    # parser.add_argument('count', type=int, required=True,
    #                     help='This field cannot be left blank')

    def get(self):
        return [test.json() for test in Test.query.all()]


class TestServices(Resource):
    # parser = reqparse.RequestParser()
    # parser.add_argument('response', type=[int], required=True,
    #                     help='This field cannot be left blank')

    def get(self, test_id):
        test = Test.get_by_id(test_id)
        return test.json()


class RavenServices(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('response', type=object, required=True,
                        help='This field cannot be left blank')

    def __init__(self):
        return

    def post(self):
        data = RavenServices.parser.parse_args()
        calculate_raven_result(data['response'])


class QuestionsServices(Resource):
    # parser = reqparse.RequestParser()
    # parser.add_argument('count', type=int, required=True,
    #                     help='This field cannot be left blank')

    def get(self):
        return [question.json() for question in Question.query.all()]


class ChoicesServices(Resource):
    # parser = reqparse.RequestParser()
    # parser.add_argument('count', type=int, required=True,
    #                     help='This field cannot be left blank')

    def get(self):
        return [choice.json() for choice in Choice.query.all()]



