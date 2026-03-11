# from flask import Flask, redirect, url_for, render_template
# from flask_restful import Api, Resource


# webapp = Flask(__name__)
# api = Api(webapp)

# class Hello(Resource):
#     def get(self, name, age):
#         return {"data": "hello",name:f"age: {age}"}
#     def post(self):
#         return {"data":"POst"}
# api.add_resource(Hello, "/hello/<string:name>/<string:age>")

# if __name__ == "__main__":
#     webapp.run(debug=True)
from flask import Flask, request, jsonify, redirect, url_for
from flask_restful import Api, Resource
from flask_cors import CORS

webapp = Flask(__name__)
CORS(webapp)
api = Api(webapp)

@webapp.route("/")
def index():
    return jsonify({
        "status": "success",
        "message": "Authentication required. Please move to login page.",
        "data": {"gotoURL": "index.html"},
        "error": [],
    }), 200

# class Login(Resource):
#     def get(self):
#         return jsonify({
#             "status": "success",
#             "message": "go in /login.",
#             "data":{"gotoURL":"login.html"},
#             "error":[],
#         })
#     def post(self):
#         data = request.get_json()
#         if not data: return {"message": "No data"}, 400
        
#         username = data.get('username')
#         password = data.get('password')

#         if username == "admin" and password == "123":
#             return {
#                 "status": "success",
#                 "message": "you're admin.",
#                 "data":{"gotoURL":"admin.html"},
#                 "error":[],
#             }, 200
        
#         return {"status": "error", "message": "Invalid credentials"}, 401
# api.add_resource(Login, "/login")
@webapp.route("/AI", methods=['POST'])
def AI():
    data = request.get_json()
    return jsonify(data)
@webapp.route("/login", methods= ['GET'])
def ReturnLoginPage():
    return jsonify({
            "status": "success",
            "message": "go in /login.",
            "data":{"gotoURL":"login.html"},
            "error":[],
        })

@webapp.route("/login", methods = ['POST'])
def ExcuteLogin():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if(username == "admin" and str(password) == '123'):
        return jsonify({
                "status": "success",
                "message": "you're admin.",
                "data":{"gotoURL":"admin.html"},
                "error":[],
            }), 200

    return jsonify({"status": "false",
                    "data": {"gotoURL": "login.html"} }), 401



if __name__ == "__main__":
    webapp.run(host="0.0.0.0",debug=True, port=5000)