# app/routes.py

from flask import render_template
from app import app
from app.models import Student, Location, Program, Student_Program, Program_Location, Participates_In, Is_About

@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)
