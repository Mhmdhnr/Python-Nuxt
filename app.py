from flask import Flask
from flask_restful import Api, Resource
import urllib as urllib
from flask_cors import CORS

from services.random_x_y import RandomXY
from services.random_names import RandomNames
from services.tests import Tests

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SERVER_NAME='flask-restful-nuxt.herokuapp.com',
    # SERVER_NAME='127.0.0.1:5000',
    SECRET_KEY='secret_xxx'
)
# params = urllib.parse.quote_plus('DRIVER={SQL Server};SERVER=localhost;DATABASE=my-api;Trusted_Connection=yes;')
# app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://lxdcspgcawenix:795dce1c1a77b56c2582bddbf92d11296d4483e04c1e82dc8db210d4bddda7bf@ec2-3-214-121-14.compute-1.amazonaws.com:5432/d5ur0qqint8ced"
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:mhmdhnr232323@127.0.0.1:5432/my-api"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
CORS(app)

@app.before_first_request
def create_tables():
    from db import db
    db.init_app(app)
    db.create_all()

@app.before_first_request
def create_tables():
    from db import db
    db.init_app(app)
    db.create_all()


# @app.after_request
# def after_request(response):
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response

class Welcome(Resource):
    def get(self):
        return "Welcome"


api.add_resource(Welcome, '/')
api.add_resource(RandomXY, '/get_random_x_y/<int:count>')
api.add_resource(RandomNames, '/get_random_names/<int:count>')
api.add_resource(Tests, '/get_tests')

if __name__ == '__main__':
    app.run(debug=True)


