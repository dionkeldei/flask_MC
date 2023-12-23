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
from flask import render_template, redirect, url_for, request, abort
from database.db import DbConn
import bcrypt
import jwt
import json
import requests


#Campañas
def loginUser():
    req = request.json
    user = request.user
    return {
        "success": True,
        "message": "User logged",
        "token": "abcdefg"
    }

def showMe():
    return request.user

def createUser():
    req = request.json
    user = request.user
    return {
        "success": True,
        "message": "User created"
    }
