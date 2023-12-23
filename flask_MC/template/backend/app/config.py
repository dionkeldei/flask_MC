'''
File: config.py
-----
File Created: Thursday, 24th August 2023 3:40:42 pm
Author: Rodolfo Gonzalez (dionkeldei@gmail.com)
-----
Copyright - 2023
'''

import os
import base64
from dotenv import load_dotenv
from sqlalchemy import create_engine

class appConfig:
    def __init__(self):
        secret_key_file = "environment/secret_key"

        with open(secret_key_file, "rb") as file:
            secret_key_bytes = file.read()

        secret_key = base64.b64encode(secret_key_bytes).decode('utf-8')
        
        dotenv_path = os.path.join(os.path.dirname(__file__), 'environment', '.env')
        load_dotenv(dotenv_path)

        # STATIC VARIABLES
        os.environ['SECRET_KEY'] = secret_key
        os.environ['MY_INTERNAL_GLOBAL_VAR'] = 'internal global var'
        #
