# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:geodb@localhost/project'
db = SQLAlchemy(app)

#this has to be done second, otherwise it's a circular import, as routes references "app"
from app import routes
