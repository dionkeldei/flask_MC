'''
File: db.py
-----
File Created: Tuesday, 20th June 2023 8:03:42 am
Author: Rodolfo Gonzalez (dionkeldei@gmail.com)
-----
Copyright - 2023
'''

import os

class DbConn:
    def __init__(self):
        self.host = os.environ.get('DB_HOST')
        self.port = os.environ.get('DB_PORT')
        self.user = os.environ.get('DB_USER')
        self.password = os.environ.get('DB_PASSWORD')
        self.database = os.environ.get('DB_DATABASE')
    
    