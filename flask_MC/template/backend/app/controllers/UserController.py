'''
File: UserController.py
-----
File Created: Tuesday, 4th July 2023 5:42:34 pm
Author: Rodolfo Gonzalez (dionkeldei@gmail.com)
-----
Copyright - 2023
'''

import os
import sys
import time
from flask import  request
import bcrypt
import jwt
import json
from models.user import findUser, allUsers, findUserWhere, setUser


def login():
    req = request.json
    password = req['password']

    users = findUserWhere({"email": req['email']})

    if len(users) == 0:
        ret = {
            "success": False,
            "token": "",
            "message": "Bad Credentials"
        }
        return ret

    user = users[0]
    stored_password = user['password']
    print(stored_password)
    print(password)

    success = bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8'))

    if success:
        payload = {
            "id": user['id'],
            "name": user['name'],
            "email": user['email']
        }

        encoded_jwt = jwt.encode(payload, os.environ.get('SECRET_KEY'), algorithm="HS256")

        ret = {
            "success": True,
            "token": encoded_jwt,
            "name": user['name'],
            "email": user['email'],
            "message": "Successfully logged in"
        }
        return ret
    else:
        ret = {
            "success": False,
            "token": "",
            "message": "Bad Credentials"
        }

        return ret

def showMe():
    return request.user

def showAllUsers():
    return {
        "success": True,
        "data": allUsers()
    }

def showUser(id):
    return {
        "success": True,
        "data": findUser(id)
    }

def createUser():
    req = request.json
    raw_password = req['password']
    password = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt())
    data = {
        "name": req['name'],
        "email": req['email'],
        "password": password.decode('utf-8')
    }
    return {
        "success": setUser(data),
        "message": "User created"
    }
