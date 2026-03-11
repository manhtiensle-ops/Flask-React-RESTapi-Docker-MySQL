from flask import Flask, request, jsonify, g, redirect, url_for
from flask_restful import Api, Resource
from flask_cors import CORS
import mysql.connector
from mysql.connector import pooling



webapp = Flask(__name__)
CORS(webapp)
api = Api(webapp)

@webapp.route("/")
def index():
    return "hell1o 111wsorddaaqqqqaaad"


class Login(Resource):
    def get(self):
        return jsonify({
            "status": "success",
            "message": "go in /login.",
            "data":{"gotoURL":"login.html"},
            "error":[],
        })
    def post(self):
        data = request.get_json()
        if not data: return {"message": "No data"}, 400
        
        username = data.get('username')
        password = data.get('password')
        cnx = mysql.connector.connect(host='db',
                                      username='root',
                                      password='password',
                                      database='LOGIN'
        )
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT username,password FROM ACCOUNT WHERE username = %s AND password = %s;",(username,password))
        user = cursor.fetchone()
        if user:
            return {"status":"ok"},200
        return {"status": "error", "message": "Invalid credentials"}, 401
api.add_resource(Login, "/login")



class TestDataBase(Resource):
    def get(self):
        u = 'hater'
        p = '123456'
        cnx = mysql.connector.connect(
            host='db',
            user='root',
            password='password',
            database='LOGIN'
        )
        cursor = cnx.cursor(dictionary=True)
        
        cursor.execute("SELECT username,password FROM ACCOUNT WHERE username = %s AND password = %s;",(u,p))
        user = cursor.fetchone()
        cursor.close()
        cnx.close()
        return user
        
api.add_resource(TestDataBase,"/data")







@webapp.route("/AI", methods=['POST'])
def AI():
    data = request.get_json()
    return jsonify(data)
