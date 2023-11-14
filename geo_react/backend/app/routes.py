# app/routes.py

from flask import render_template, jsonify
from app import app
from app.models import Student

@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)

@app.route('/test_student')
def test_student():
    students = Student.query.all()
    res = [{'student_email':student.student_email,
            'major':student.major,
            'primary_reason':student.primary_reason,
            'language_proficiency':student.language_proficiency} for student in students]
    return jsonify(res)
