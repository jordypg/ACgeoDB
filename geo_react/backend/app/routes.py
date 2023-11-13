# app/routes.py

from flask import render_template
from app import app
from app.models import Student

@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)
