from flask import Flask, request, jsonify, g, redirect, url_for
from flask_restful import Api, Resource
from flask_cors import CORS
import mysql.connector
from mysql.connector import pooling
from api.loginapi import Login
from config import Config
from flask_jwt_extended import JWTManager


webapp = Flask(__name__)

CORS(webapp)
api = Api(webapp)
webapp.config["JWT_SECRET_KEY"] = "manhtien"  # Change this!
jwt = JWTManager(webapp)


api.add_resource(Login,"/login")


print(Config.JWT_SECRET_KEY)


@webapp.route("/")
def index():
    return "hell1o 111wsorddaaqqqqaaad"

