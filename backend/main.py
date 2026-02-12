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

# Route truyền thống trả về chuỗi văn bản
@webapp.route("/home/<username>")
def home(username):
    return f"hello {username}"

@webapp.route("/")
def index():
    return jsonify({
        "action": "redirect",
        "target": "login.html",
        "message": "Authentication required. Please move to login page."
    }), 200

    

class Login(Resource):
    def post(self):
        data = request.get_json()
        if not data: return {"message": "No data"}, 400
        
        username = data.get('username')
        password = data.get('password')

        if username == "admin" and password == "123":
            return {
                "status": "success",
                # SỬA Ở ĐÂY: Trả về tên file HTML ở thư mục frontend
                "redirect_url": "admin.html" 
            }, 200
        
        return {"status": "error", "message": "Invalid credentials"}, 401

api.add_resource(Login, "/login")

if __name__ == "__main__":
    webapp.run(debug=True, port=5000)