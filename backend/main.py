from flask import Flask, request, jsonify, g, redirect, url_for
from flask_restful import Api
from flask_cors import CORS
from mysql.connector import pooling
from api.loginapi import Login
from config import Config
from flask_jwt_extended import JWTManager
from api.checkPermissionAPI import checkPermissionAPI
from api.logoutapi import Logout
webapp = Flask(__name__)

CORS(webapp)
api = Api(webapp)
webapp.config["JWT_SECRET_KEY"] = "manhtien" 
webapp.config['JWT_TOKEN_LOCATION'] = ['cookies']
webapp.config['JWT_ACCESS_COOKIE_NAME'] = 'login'
webapp.config['JWT_ACCESS_CSRF_COOKIE_NAME'] = 'login'
webapp.config['JWT_COOKIE_CSRF_PROTECT'] = False 
webapp.config['JWT_CSRF_IN_COOKIES'] = False     
jwt = JWTManager(webapp)


api.add_resource(Login,"/api/login")
api.add_resource(checkPermissionAPI,"/checkPermission")
api.add_resource(Logout,"/api/logout")



@webapp.route("/")
def index():
    return "hell1o 111wsorddaaqqqqaaad"

