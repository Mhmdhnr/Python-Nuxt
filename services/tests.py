from flask_restful import Resource, reqparse
from models.tests import Test, Question, Choice
from business.tests import calculate_raven_result, calculate_mbti_result, calculate_holland_result,\
    calculate_johnson_result, calculate_glasser_result, calculate_stephen_result
from business.user_test import get_user_test_results
from flask_login import login_required


class TestResults(Resource):
    def get(self):
        return get_user_test_results()

class TestsServices(Resource):

    def get(self):
        return [test.json() for test in Test.query.all()]


class TestServices(Resource):

    def get(self, test_id):
        test = Test.get_by_id(test_id)
        return test.json()


class RavenServices(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('clientAnswers', type=str, required=True,
                        help='This field cannot be left blank')

    def __init__(self):
        return

    # @login_required
    def post(self):
        data = RavenServices.parser.parse_args()
        return calculate_raven_result(data['clientAnswers'])


class MBTIServices(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('clientAnswers', type=str, required=True,
                        help='This field cannot be left blank')

    def __init__(self):
        return

    # @login_required
    def post(self):
        data = MBTIServices.parser.parse_args()
        return calculate_mbti_result(data['clientAnswers'])

class HollandServices(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('clientAnswers', type=str, required=True,
                        help='This field cannot be left blank')

    def __init__(self):
        return

    # @login_required
    def post(self):
        data = HollandServices.parser.parse_args()
        return calculate_holland_result(data['clientAnswers'])


class JohnsonServices(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('clientAnswers', type=str, required=True,
                        help='This field cannot be left blank')

    def __init__(self):
        return

    # @login_required
    def post(self):
        data = JohnsonServices.parser.parse_args()
        return calculate_johnson_result(data['clientAnswers'])


class GlasserServices(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('clientAnswers', type=str, required=True,
                        help='This field cannot be left blank')

    def __init__(self):
        return

    def post(self):
        data = GlasserServices.parser.parse_args()
        return calculate_glasser_result(data['clientAnswers'])


class StephenServices(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('clientAnswers', type=str, required=True,
                        help='This field cannot be left blank')

    def __init__(self):
        return

    def post(self):
        data = StephenServices.parser.parse_args()
        return calculate_stephen_result(data['clientAnswers'])


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



