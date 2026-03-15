from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from api.loginapi import Login

app = Flask(__name__)
app.config.from_object(Config) # Load toàn bộ cấu hình từ class Config

# Khởi tạo các module mở rộng
api = Api(app)
jwt = JWTManager(app) # Đối tượng này sẽ quản lý việc ký và kiểm tra token

api.add_resource(Login, '/login')


app.run(debug=True)