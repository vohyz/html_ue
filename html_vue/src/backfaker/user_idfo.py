from flask import Flask
from flask_cors import CORS, cross_origin
from flask_restful import Api, Resource, reqparse
import datetime
import time
import pymysql

app = Flask(__name__)
api = Api(app)
cors = CORS(app)

# 创建订单类
class Register(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', type=str)
        self.parser.add_argument('pass', type=str)
        self.parser.add_argument('checkPass', type=str)
        self.parser.add_argument('age', type=str)
        self.parser.add_argument('sex', type=str)

    def post(self):
        data = self.parser.parse_args()
        print(data)
        # rst = self.create(params)
        return {'rst': 'ok'}

class Login(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', type=str)
        self.parser.add_argument('pass', type=str)

    def post(self):
        data = self.parser.parse_args()
        print(data)
        # rst = self.create(params)
        return {'rst': 'ok'}

api.add_resource(Register, '/register')
api.add_resource(Login, '/login')

if __name__ == '__main__':
    app.run(debug=True, port= 5001)