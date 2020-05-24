from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

api.add_resource(Task, '/card/<string:name>')
api.add_resource(TaskList, '/board')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
