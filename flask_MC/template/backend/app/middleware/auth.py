'''
File: auth.py
-----
File Created: Tuesday, 4th July 2023 8:08:52 pm
Author: Rodolfo Gonzalez (dionkeldei@gmail.com)
-----
Copyright - 2023
'''

import os
from flask import request, abort, Response
from database.db import DbConn
import bcrypt
import jwt
import json
import re

def check_open_route(route_to_check, json_file_path="middleware/openRoutes.json"):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        if "routes" in data:
            for route_pattern in data["routes"]:
                if re.match(route_pattern.replace("{variable}", r"\d+"), route_to_check):
                    return True
    return False

def auth():
    if not check_open_route(request.path) and not request.path.startswith('/static/'):
        if request.method == 'OPTIONS':
            return Response()
        if request.path not in ['/user/login'] and request.method != 'OPTIONS':
            try:
                user = jwt.decode(request.headers.get('Authorization'), os.environ.get('SECRET_KEY'), algorithms=["HS256"])
            except:
                abort(401, description="You dont have access to this resource.")
            # To get the user in routes, use this
            request.user = user
    

    
