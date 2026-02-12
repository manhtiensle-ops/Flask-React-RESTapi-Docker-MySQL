from flask import Flask, redirect, url_for, render_template
from flask_restful import Api, Resource


webapp = Flask(__name__)
api = Api(webapp)

class Hello(Resource):
    def get(self):
        return {"data": "hello"}
api.add_resource(Hello, "/hello")

webapp.run(debug=True)