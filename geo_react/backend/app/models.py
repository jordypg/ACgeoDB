# app/models.py

# from app import db
# from sqlalchemy.engine import URL
from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.orm import declarative_base

db = declarative_base()

class Student(db):
        __tablename__ = 'student'
        student_email = Column(String(255), primary_key=True, nullable=False)
        primary_reason = Column(String(500))
        language_proficiency = Column(String(50))

class Major(db):
	__tablename__ = 'major'
	student_email = Column(String(255), primary_key=True, nullable=False)
	major_name = Column(String(50))

class Program(db):
	__tablename__ = 'program'
	program_name = Column(String(255), primary_key=True, nullable=False)

class Personal_Reflection(db):
	__tablename__ = 'personal_reflection'
	student_email = Column(String(255), primary_key=True, nullable=False)
	program_name = Column(String(255))
	term = Column(String(255))
	pr_id = Column(String(50))


class Student_Program(db):
	__tablename__ = 'student_program'
	# id = Column(Integer, primary_key=True, nullable=False)
	student_email = Column(String(255), primary_key=True, nullable = False)
	program_name = Column(String(255), primary_key = True, nullable = False)
	term = Column(String(255))

# class Program_Location(db.Model):
# 	__tablename__ = 'program_location'
# 	program_name = db.Column(db.String(255), primary_key=True, nullable=False)
# 	location_name = db.Column(db.String(255))

# class Participates_In(db.Model):
# 	__tablename__ = 'participates_in'
# 	id = db.Column(db.Integer, primary_key=True, nullable=False)
# 	student_email = db.Column(db.String(255))
# 	program_name = db.Column(db.String(255))
# 	term = db.Column(db.String(255))
# 	language_proficiency_after = db.Column(db.String(255))
# 	amount_spent = db.Column(db.Integer)
# 	city_affordability = db.Column(db.Text)
# 	extracurriculars = db.Column(db.Text)
# 	courses_taken = db.Column(db.Text)
# 	courses_type = db.Column(db.String(255))
# 	influencing_factors = db.Column(db.String(255))
# 	attitudes_diff = db.Column(db.Boolean)
# 	attitudes_diff_comments = db.Column(db.Text)
# 	orientation_description = db.Column(db.Text)
# 	res_staff_avail = db.Column(db.Boolean)
# 	res_staff_comment = db.Column(db.Text)
# 	housing_acc = db.Column(db.Boolean)
# 	housing_acc_comment = db.Column(db.Text)
# 	academic_exc_avail = db.Column(db.Boolean)
# 	academic_exc_rating = db.Column(db.String(255))
# 	academic_exc_comments = db.Column(db.Text)
# 	leisure_exc_avail = db.Column(db.Boolean)
# 	leisure_exc_rating = db.Column(db.String(255))
# 	leisure_exc_comments = db.Column(db.Text)

# class Is_About(db.Model):
# 	__tablename__ = 'is_about'
# 	id = db.Column(db.Integer, primary_key=True, nullable=False)
# 	pr_id = db.Column(db.Integer)
# 	student_name = db.Column(db.String(255))
# 	program_name = db.Column(db.String(255))
# 	goals_reflections = db.Column(db.Text)
# 	term = db.Column(db.String(255))
# 	growth = db.Column(db.Text)
# 	challenges = db.Column(db.Text)
# 	new_perspectives = db.Column(db.Text)
# 	recomendation_rating = db.Column(db.Integer)
# 	recommendation_comments = db.Column(db.Text)
