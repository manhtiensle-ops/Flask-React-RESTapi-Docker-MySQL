from flask import request, jsonify
from flask_restful import Resource

from flask_jwt_extended import create_access_token, set_access_cookies, jwt_required, get_jwt_identity,get_jwt

class checkPermissionAPI(Resource):
    @jwt_required()
    def get(self):
     current_user = get_jwt_identity()
     if not current_user:
        return{"error":"ll"},401
     return {"ok":"ok"},200
            
