from flask_restful import Resource, reqparse
from models.tests import Test, Question, Choice
from business.tests import calculate_raven_result, calculate_mbti_result, calculate_holland_result,calculate_johnson_result
from flask_login import login_required


class TestsServices(Resource):
    # parser = reqparse.RequestParser()
    # parser.add_argument('count', type=int, required=True,
    #                     help='This field cannot be left blank')

    def get(self):
        return [test.json() for test in Test.query.all()]


class TestServices(Resource):

    @login_required
    def get(self, test_id):
        test = Test.get_by_id(test_id)
        return test.json()


class RavenServices(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('clientAnswers', type=str, required=True,
                        help='This field cannot be left blank')

    def __init__(self):
        return

    def post(self):
        data = RavenServices.parser.parse_args()
        return calculate_raven_result(data['clientAnswers'])


class MBTIServices(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('clientAnswers', type=str, required=True,
                        help='This field cannot be left blank')

    def __init__(self):
        return

    def post(self):
        data = MBTIServices.parser.parse_args()
        return calculate_mbti_result(data['clientAnswers'])

class HollandServices(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('clientAnswers', type=str, required=True,
                        help='This field cannot be left blank')

    def __init__(self):
        return

    def post(self):
        data = HollandServices.parser.parse_args()
        return calculate_holland_result(data['clientAnswers'])


class JohnsonServices(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('clientAnswers', type=str, required=True,
                        help='This field cannot be left blank')

    def __init__(self):
        return

    def post(self):
        data = JohnsonServices.parser.parse_args()
        return calculate_johnson_result(data['clientAnswers'])


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



