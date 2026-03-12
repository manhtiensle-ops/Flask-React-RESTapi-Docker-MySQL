from flask import request, jsonify
from flask_restful import Resource
import mysql.connector

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
            return {"status":"ok","goto":"/controlpanel"},200
        return {"status": "error", "message": "Invalid credentials"}, 401