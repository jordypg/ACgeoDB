# app/routes.py
from sqlalchemy import text
from flask import render_template, jsonify, request
from app import app, db
from .randomnames import generate_random_name

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

#/get_backside?pgr_id={PROGRAM ID}
@app.route('/get_all_cards', methods=['GET'])
def get_all_cards():
    query = '''
    SELECT pr.pgr_id,
           pr.student_email,
           h.program_name AS program,
           l.country,
           MAX(CASE WHEN m.row_num = 1 THEN m.major_name ELSE '' END) AS major_1,
           MAX(CASE WHEN m.row_num = 2 THEN m.major_name ELSE '' END) AS major_2,
           MAX(CASE WHEN m.row_num = 3 THEN m.major_name ELSE '' END) AS major_3
    FROM program_reflection pr
    LEFT JOIN (
        SELECT student_email, major_name,
               ROW_NUMBER() OVER(PARTITION BY student_email ORDER BY major_name) AS row_num
        FROM has_major
    ) m ON pr.student_email = m.student_email
    LEFT JOIN hosted_in h ON pr.program_name = h.program_name
    LEFT JOIN location l ON h.location_name = l.location_name
    GROUP BY pr.pgr_id, pr.student_email, h.program_name, l.country;
    '''
    result = db.session.execute(text(query))
    
    # Extracting required columns from the result
    rows = [
        {
            'pgr_id': row.pgr_id,
            'student_email': row.student_email,
            'program': row.program,
            'country': row.country,
            'majors': [row.major_1, row.major_2, row.major_3],
            'random_name': generate_random_name()  # Add a random name field
        }
        for row in result
    ]

    return jsonify(rows)
