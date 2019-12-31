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
        return {'rst': data['name']}

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
                    'id':str(i),
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
class Task(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('task_id', type=str)

    def post(self):
        data = self.parser.parse_args()
        print(data)
        if data['task_id'] == '0':
            # rst = self.create(params)
            return {
                'publisher':'1652514',
                'title': '任务名',
                'info':'任务详细介绍，详细详细xxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
                'bonus':'150',
                'tags':['英雄联盟', '守望先锋', '网游', '娱乐', '休闲'],
                'createtime':'2019-12-28 21:06:03'
                }
        else:
            return {
                'publisher':'1752514',
                'title': '任务名',
                'info':'任务详细介绍，详细详细xxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
                'bonus':'150',
                'tags':['英雄联盟', '守望先锋', '网游', '娱乐', '休闲'],
                'createtime':'2019-12-28 21:06:03'
                }

api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
api.add_resource(Order, '/order')
api.add_resource(Task, '/task')

if __name__ == '__main__':
    app.run(debug=True, port= 5001)
