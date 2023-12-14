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

@app.route('/get_all_programs', methods=['GET'])
def get_all_programs():
    query = '''
    SELECT 
        h.program_name,
        h.location_name,
        pr.term_id, pr.recommendation_rating, pr.recommendation_comments,
        f.amount_spent, f.city_affordability, f.housing_acc, f.housing_acc_comments,
        s.attitudes_diff, s.attitudes_diff_comments, s.res_staff, s.res_staff_comments, s.leisure_exc_avail, s.leisure_exc_rating, s.leisure_exc_comments,
        aa.academic_exc_avail, aa.academic_exc_rating, aa.academic_exc_comments, aa.influencing_factors, aa.orientation_description
    FROM 
        program_reflection pr
    LEFT JOIN 
        hosted_in h ON pr.program_name = h.program_name
    LEFT JOIN 
        is_about_financial_factors f ON pr.pgr_id = f.pgr_id
    LEFT JOIN 
        is_about_social_factors s ON pr.pgr_id = s.pgr_id
    LEFT JOIN 
        is_about_academic_factors aa ON pr.pgr_id = aa.pgr_id;
    '''
    result = db.session.execute(text(query))
    
    # Creating a dictionary of dictionaries
    programs = {}
    for row in result:
        program_name = row.program_name
        if program_name not in programs:
            programs[program_name] = []

        programs[program_name].append({
            'program_name': row.program_name,
            'location_name': row.location_name,
            'term_id': row.term_id,
            'recommendation_rating': row.recommendation_rating,
            'recommendation_comments': row.recommendation_comments,
            'amount_spent': row.amount_spent,
            'city_affordability': row.city_affordability,
            'housing_acc': row.housing_acc,
            'housing_acc_comments': row.housing_acc_comments,
            'attitudes_diff': row.attitudes_diff,
            'attitudes_diff_comments': row.attitudes_diff_comments,
            'res_staff': row.res_staff,
            'res_staff_comments': row.res_staff_comments,
            'leisure_exc_avail': row.leisure_exc_avail,
            'leisure_exc_rating': row.leisure_exc_rating,
            'leisure_exc_comments': row.leisure_exc_comments,
            'academic_exc_avail': row.academic_exc_avail,
            'academic_exc_rating': row.academic_exc_rating,
            'academic_exc_comments': row.academic_exc_comments,
            'influencing_factors': row.influencing_factors,
            'orientation_description': row.orientation_description
        })

    # Convert the dictionary to a JSON-compatible format
    return jsonify(programs)


