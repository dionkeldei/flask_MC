'''
File: app.py
-----
File Created: Monday, 19th June 2023 9:07:18 pm
Author: Rodolfo Gonzalez (dionkeldei@gmail.com)
-----
Copyright - 2023
'''

from flask import Flask, render_template, abort, request, send_from_directory
from flask_cors import CORS, cross_origin
from config import appConfig
from database.db_conn import db, dbConfig

appConfig()

from middleware.auth import auth
from routes.user_bp import user_bp

app = Flask(__name__)
CORS(app, expose_headers='Authorization')

app.config.from_object('config')

app.config['SQLALCHEMY_DATABASE_URI'] = dbConfig()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# BLUEPRINTS
app.register_blueprint(user_bp, url_prefix='/users')

@app.before_request
def middleware():
    if request.method == 'OPTIONS':
        response = "{'message': 'OK'}"
        return response
    auth() 

@app.route('/')
def index():
    return 'Cannot GET'

@app.route('/static/<path:path>')
def send_report(path):
    return send_from_directory('static', path)