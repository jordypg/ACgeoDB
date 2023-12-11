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

#/get_backside?pgr_id={PROGRAM ID}
@app.route('/get_backside', methods=['GET'])
def get_backside():
    pgr_id = request.args['pgr_id']
    backside_query = '''select distinct program_reflection.term_id, primary_reason, courses_taken, housing_acc, housing_acc_comments,
                        academic_exc_rating, academic_exc_comments, leisure_exc_rating, leisure_exc_comments, city_affordability,
                        amount_spent, attitudes_diff, attitudes_diff_comments, growth, challenges, new_perspectives
                        from public.program_reflection
                        join public.is_about_academic_factors
                        on program_reflection.pgr_id = is_about_academic_factors.pgr_id
                        join public.is_about_financial_factors
                        on program_reflection.pgr_id = is_about_financial_factors.pgr_id
                        join public.is_about_social_factors
                        on program_reflection.pgr_id = is_about_social_factors.pgr_id
                        join public.personal_reflection
                        on program_reflection.student_email = personal_reflection.student_email
                        and program_reflection.program_name = personal_reflection.program_name
                        and program_reflection.term_id = personal_reflection.term_id
                        join public.participates_in
                        on program_reflection.student_email = participates_in.student_email
                        and program_reflection.program_name = participates_in.program_name
                        and program_reflection.term_id = participates_in.term_id
                        join public.student
                        on participates_in.student_email = student.student_email
                        where program_reflection.pgr_id LIKE ''' + f"'{pgr_id}' ;"
    

    backside = db.session.execute(text(backside_query)).all()
    backside = backside[0]._asdict()

    res = [{'term_id' : backside['term_id'],
            'primary_reason' : backside['primary_reason'],
            'courses_taken' : backside['courses_taken'],
            'housing_acc' : backside['housing_acc'],
            'housing_acc_comments' : backside['housing_acc_comments'],
            'academic_exc_rating' : backside['academic_exc_rating'],
            'academic_exc_comments' : backside['academic_exc_comments'],
            'leisure_exc_rating' : backside['leisure_exc_rating'],
            'leisure_exc_comments' : backside['leisure_exc_comments'],
            'city_affordability' : backside['city_affordability'],
            'amount_spent' : backside['amount_spent'],
            'attitudes_diff' : backside['attitudes_diff'],
            'attitudes_diff_comments' : backside['attitudes_diff_comments'],
            'growth' : backside['growth'],
            'challenges' : backside['challenges'],
            'new_perspectives' : backside['new_perspectives']
            }]    
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
