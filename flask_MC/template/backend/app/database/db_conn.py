import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import current_app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def dbConfig():
    user = os.environ.get('DB_USER')
    password = os.environ.get('DB_PASSWORD')
    host = os.environ.get('DB_HOST')
    database = os.environ.get('DB_DATABASE')
    port = os.environ.get('DB_PORT')
    return f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'
