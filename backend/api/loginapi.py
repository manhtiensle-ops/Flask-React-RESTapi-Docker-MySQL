from flask_restful import Api, Resource

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

        if username == "admin" and password == "123":
            return {
                "status": "success",
                "message": "you're admin.",
                "data":{"gotoURL":"admin.html"},
                "error":[],
            }, 200
        
        return {"status": "error", "message": "Invalid credentials"}, 401
api.add_resource(Login, "/login")