'''
File: user_bp.py
-----
File Created: Tuesday, 4th July 2023 5:39:47 pm
Author: Rodolfo Gonzalez (dionkeldei@gmail.com)
-----
Copyright - 2023
'''

from flask import Blueprint
from controllers.UserController import *
user_bp = Blueprint('user_bp', __name__)

# User

user_bp.route('/', methods=['GET'])(showAllUsers)
user_bp.route('/<int:id>', methods=['GET'])(showUser)
user_bp.route('/login', methods=['POST'])(login)
user_bp.route('/me', methods=['GET','OPTIONS'])(showMe)
user_bp.route('/create', methods=['POST','OPTIONS'])(createUser)


