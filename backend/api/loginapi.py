from flask import request, jsonify
from flask_restful import Resource
import mysql.connector
from flask_jwt_extended import create_access_token, set_access_cookies, jwt_required, get_jwt_identity,get_jwt



class Login(Resource):
    @jwt_required(optional=True)
    def get(self):
        current_user = get_jwt_identity()
        if current_user:
            claims = get_jwt()
            if claims.get("user_agent") == request.headers.get('User-Agent'):
                return jsonify({
                    "status": "success",
                    "user":current_user,
                    "message": f"Bạn đã đăng nhập với tài khoản {current_user}!",
                    "data": {"gotoURL": "/"}, # Điều hướng thẳng vào trong
                    "error": []
                })

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
        user_agent = request.headers.get('User-Agent')

        
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
            
            access_token = create_access_token(
                identity=username, 
                additional_claims={"user_agent": user_agent}
            )
            
            response = jsonify({
                "status": "ok", 
                "data": {"gotoURL": "/"},
                "message": "Đăng nhập thành công!",
                "username": username
            })

            set_access_cookies(response, access_token)
            return response
        return {"status": "error", "message": "Invalid credentials"}, 401