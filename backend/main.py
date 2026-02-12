from flask import Flask, redirect, url_for, render_template
from flask_restful import Api, Resource


webapp = Flask(__name__)
api = Api(webapp)

class Hello(Resource):
    def get(self, name, age):
        return {"data": "hello",name:f"age: {age}"}
    def post(self):
        return {"data":"POst"}
api.add_resource(Hello, "/hello/<string:name>/<string:age>")

webapp.run(debug=True)