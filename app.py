from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS
from flask_login import LoginManager

from models.user import User
from services.user import SignInUp, Token, SignOut, UserInfo
from services.random_x_y import RandomXY
from services.random_names import RandomNames
from services.tests import TestsServices, QuestionsServices, ChoicesServices, TestServices, RavenServices, MBTIServices\
    , HollandServices, JohnsonServices


app = Flask(__name__)
app.config.update(
    DEBUG=True,
    # SERVER_NAME='flask-restful-nuxt.herokuapp.com',
    SERVER_NAME='127.0.0.1:5000',
    SECRET_KEY='secret_xxx'
)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SESSION_COOKIE_SAMESITE'] = 'None'
app.config['SESSION_COOKIE_SECURE'] = 'True'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://lxdcspgcawenix:795dce1c1a77b56c2582bddbf92d11296d4483e04c1e82dc8db210d4bddda7bf@ec2-3-214-121-14.compute-1.amazonaws.com:5432/d5ur0qqint8ced"
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:mhmdhnr232323@127.0.0.1:5432/my-api"


api = Api(app)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True,)
login_manager = LoginManager()
login_manager.init_app(app)

# @app.after_request
# def after_request(response):
    # response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
    # response.headers.add('Accept', 'application/json')
    # response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,Access-Control-Allow-Methods,Access-Control-Allow-Origin,access-control-allow-credentials,Access-Control-Allow-Headers')
    # response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    # response.headers.add('Access-Control-Allow-Credentials', 'true')
    # return response


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


@app.before_first_request
def create_tables():
    from db import db
    db.init_app(app)
    db.create_all()


class Welcome(Resource):
    def get(self):
        return "Welcome"


api.add_resource(Welcome, '/')
api.add_resource(RandomXY, '/get_random_x_y/<int:count>')
api.add_resource(Token, '/send_token')
api.add_resource(UserInfo, '/info')
api.add_resource(SignInUp, '/sign')
api.add_resource(SignOut, '/sign_out')
api.add_resource(RandomNames, '/get_random_names/<int:count>')
api.add_resource(TestsServices, '/get_tests')
api.add_resource(TestServices, '/get_test/<int:test_id>')
api.add_resource(QuestionsServices, '/get_questions')
api.add_resource(ChoicesServices, '/get_choices')
api.add_resource(RavenServices, '/post_raven_response')
api.add_resource(MBTIServices, '/post_mbti_response')
api.add_resource(HollandServices, '/post_holland_response')
api.add_resource(JohnsonServices, '/post_johnson_response')


if __name__ == '__main__':
    app.run(debug=True)


