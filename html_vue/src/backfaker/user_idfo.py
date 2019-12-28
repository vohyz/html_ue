from flask import Flask
from flask_cors import CORS, cross_origin
from flask_restful import Api, Resource, reqparse
import datetime
import time

app = Flask(__name__)
api = Api(app)
cors = CORS(app)

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

class Order(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('order_id', type=str)
        self.parser.add_argument('user_id', type=str)
        self.parser.add_argument('order_type', type=str)

    def get(self):
        data = self.parser.parse_args()
        print(data)
        n = 0
        price = '1'
        if data['order_type'] == 'publiced':
            n = 4
            price = '已发布'
            a = '小明'
            b = '小红'
        elif data['order_type'] == 'caogao':
            n = 2
            price = '草稿箱'
            a = '小明'
            b = '小红'
        elif data['order_type'] == 'ing':
            n = 5
            price = '进行中'
            a = '小红'
            b = '小明'
        elif data['order_type'] == 'achieved':
            n = 6
            price = '已完成'
            a = '小红'
            b = '小明'
        params = {
            'code': 200,
            'message': 'success',
            'works': [
                {
                    'title': 'work' + str(i),
                    'beinger': a,
                    'ender': b,
                    'price': price
                }
                for i in range(n)
            ]
        }    
        # rst = self.create(params)
        return params

    def post(self):
        data = self.parser.parse_args()
        print(data)
        # rst = self.create(params)
        return {'rst': 'ok'}

api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
api.add_resource(Order, '/order')

if __name__ == '__main__':
    app.run(debug=True, port= 5001)
