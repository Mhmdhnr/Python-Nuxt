from flask_restful import Resource
from business.user_test import get_user_test_results
from flask_login import login_required


class UserTestResults(Resource):
    @login_required
    def get(self):
        return get_user_test_results()

