# app/routes.py

from flask import render_template, jsonify
from app import app, db
from app.models import Student, Student_Program, Program

@app.route('/getAllStudents')
def index():
    students = db.session.query(Student).all()
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

@app.route('/getStudents', methods=['GET'])
def getStudents():
    students = (
            db.session.query(Student.student_email)
            .join(Student_Program, Student.student_email == Student_Program.student_email)
            .filter(Student_Program.program_name == 'DIS Copenhagen')
            .all()
    )
    res = [student.student_email for student in students]
    print(res)
    return jsonify([{'student_email' : student.student_email} for student in students])

@app.route('/getPrograms', methods=['GET'])
def getPrograms():
    programs = (
            db.session.query(Program)
            .join(Student_Program, Program.program_name == Student_Program.program_name)
            .join(Student, Student.student_email == Student_Program.student_email)
            .filter(Student.major.ilike('%ECON%'))
            .all()
    )
    print(programs)
    return jsonify([{'program_name' : program.program_name} for program in programs])
