from flask import Flask, request, jsonify, g, redirect, url_for
from flask_restful import Api, Resource
from flask_cors import CORS
import mysql.connector
from mysql.connector import pooling
from api.loginapi import Login


webapp = Flask(__name__)
CORS(webapp)
api = Api(webapp)
api.add_resource(Login,"/login")




@webapp.route("/")
def index():
    return "hell1o 111wsorddaaqqqqaaad"

@webapp.route("/AI", methods=['POST'])
def AI():
    data = request.get_json()
    return jsonify(data)
