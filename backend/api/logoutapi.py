from flask import request, jsonify
from flask_restful import Resource

from flask_jwt_extended import unset_jwt_cookies



class Logout(Resource):
    def post(self):
        response = jsonify({"msg": "Successfully logged out"})
        unset_jwt_cookies(response)
        return response