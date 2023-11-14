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

@app.route('/test_all')
def test_all():
    res = [{'program_name': 'Program 1',
            'country':'Country 1',
            'influencing_factors':'Factor 1',
            'primary_language':'Language 1',
            'amount_spent':'USD 1',
            'extracurriculars':'Activity 1',
            'recommendation_rating':'1',
            'primary_reason':'Reason 1',
            'major':'Major 1'},
            {'program_name': 'Program 2',
            'country':'Country 2',
            'influencing_factors':'Factor 2',
            'primary_language':'Language 2',
            'amount_spent':'USD 2',
            'extracurriculars':'Activity 2',
            'recommendation_rating':'2',
            'primary_reason':'Reason 2',
            'major':'Major 2'}]
    return jsonify(res)
