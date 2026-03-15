from flask import request, jsonify
from flask_restful import Resource
import mysql.connector
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager


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
        cursor.close()
        cnx.close()
        if user:
            access_token = create_access_token(identity=user['username'])
            return {"status":"ok","goto":"/controlpanel", 'data': access_token},200
        return {"status": "error", "message": "Invalid credentials"}, 401