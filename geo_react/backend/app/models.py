# app/models.py

# from app import db
# from sqlalchemy.engine import URL
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import declarative_base

db = declarative_base()

class Student(db):
        __tablename__ = 'student'
        student_email = Column(String(255), nullable=False, primary_key=True)
        primary_reason = Column(db.Text)

class Major(db):
	__tablename__ = 'major'
	major_name = Column(String(255), nullable=False, primary_key=True)

class Has_Major(db):
	__tablename__ = 'has_major'
	student_email = Column(String(255), db.ForeignKey('student.student_email'), nullable=False, primary_key=True)
	major_name = Column(String(255), db.ForeignKey('major.major_name'), nullable=True, primary_key=True)

	student = db.relationship('Student')
	major = db.relationship('Major')
#question for Prof. Riondato: include a backref here?

class Program(db):
	__tablename__ = 'program'
	program_name = Column(String(255), nullable=False, primary_key=True)

class Term(db):
	__tablename__ = 'term'
	term_id = Column(String(255), nullable=False, primary_key=True)

class Participates_In(db):
	__tablename__ = 'participates_in'
	student_email = Column(String(255), db.ForeignKey('student.student_email'), nullable=False, primary_key=True)
	program_name = Column(String(255), db.ForeignKey('program.program_name'), nullable=False, primary_key=True)
	term_id = Column(String(255), db.ForeignKey('term.term_id'), nullable=False, primary_key=True)

	student = db.relationship('Student')
	program = db.relationship('Program')
	term = db.relationship('Term')


class Personal_Reflection(db):
	__tablename__ = 'personal_reflection'
	student_email = Column(String(255), db.ForeignKey('student.student_email'), nullable=False, primary_key=True)
	program_name = Column(String(255), db.ForeignKey('program.program_name'), nullable=False, primary_key=True)
	term_id = Column(String(255), db.ForeignKey('term.term_id'), nullable=False, primary_key=True)
	pr_id = Column(String(255), nullable=False, primary_key=True)
	goals_reflection = db.Column(db.Text)
	growth = db.Column(db.Text)
	challenges = db.Column(db.Text)
	new_perspectives = db.Column(db.Text)
	language_proficiency_before = db.Column(db.Text)
	language_proficiency_after = db.Column(db.Text)

	student = db.relationship('Student')
	program = db.relationship('Program')
	term = db.relationship('Term')


class Program_Reflection(db):
	__tablename__ = 'program_reflection'
	student_email = Column(String(255), db.ForeignKey('student.student_email'), nullable=False, primary_key=True)
	program_name = Column(String(255), db.ForeignKey('program.program_name'), nullable=False, primary_key=True)
	term_id = Column(String(255), db.ForeignKey('term.term_id'), nullable=False, primary_key=True)
	pgr_id = Column(String(255), unique=True, primary_key=True)
	recommendation_rating = db.Column(db.Text)
	recommendation_comments = db.Column(db.Text)

	student = db.relationship('Student')
	program = db.relationship('Program')
	term = db.relationship('Term')

class Is_About_Academic_Factors(db.Model):
	__tablename__ = 'is_about_academic_factors'
	pgr_id = db.Column(db.String(255), db.ForeignKey('program_reflection.pgr_id'), nullable=False, primary_key=True)
	program_name = db.Column(db.String(255), db.ForeignKey('program.program_name'), nullable=False)
	term_id = db.Column(db.String(255), db.ForeignKey('term.term_id'), nullable=False)
	courses_taken = db.Column(db.Text)
	courses_type = db.Column(db.Text)
	academic_exc_avail = db.Column(db.Text)
	academic_exc_rating = db.Column(db.Text)
	academic_exc_comments = db.Column(db.Text)
	influencing_factors = db.Column(db.Text)
	orientation_description = db.Column(db.Text)

	program_reflection = db.relationship('Program_Reflection')
	program = db.relationship('Program')
	term = db.relationship('Term')


class Is_About_Financial_Factors(db.Model):
	__tablename__ = 'is_about_financial_factors'
	pgr_id = db.Column(db.String(255), db.ForeignKey('program_reflection.pgr_id'), nullable=False, primary_key=True)
	program_name = db.Column(db.String(255), db.ForeignKey('program.program_name'), nullable=False)
	term_id = db.Column(db.String(255), db.ForeignKey('term.term_id'), nullable=False)
	amount_spent = db.Column(db.String(255))
	city_affordability = db.Column(db.Text)
	housing_acc = db.Column(db.Text)
	housing_acc_comments = db.Column(db.Text)

	program_reflection = db.relationship('Program_Reflection')
	program = db.relationship('Program')
	term = db.relationship('Term')

class Is_About_Social_Factors(db.Model):
	__tablename__ = 'is_about_social_factors'
	pgr_id = db.Column(db.String(255), db.ForeignKey('program_reflection.pgr_id'), nullable=False, primary_key=True)
	program_name = db.Column(db.String(255), db.ForeignKey('program.program_name'), nullable=False)
	term_id = db.Column(db.String(255), db.ForeignKey('term.term_id'), nullable=False)
	extracurriculars = db.Column(db.Text)
	attitudes_diff = db.Column(db.Text)
	attitudes_diff_comments = db.Column(db.Text)
	res_staff = db.Column(db.Text)
	res_staff_comments = db.Column(db.Text)
	leisure_exc_avail = db.Column(db.Text)
	leisure_exc_rating = db.Column(db.Text)
	leisure_exc_comments = db.Column(db.Text)

	program_reflection = db.relationship('Program_Reflection')
	program = db.relationship('Program')
	term = db.relationship('Term')

class Location(db.Model):
	__tablename__ = 'location'
	location_name = db.Column(db.String(255), nullable=False, primary_key=True)
	primary_lang_spoken = db.Column(db.String(255))
	country = db.Column(db.String(255))

class Hosted_In(db.Model):
	__tablename__ = 'hosted_in'
	program_name = db.Column(db.String(255), db.ForeignKey('program.program_name'), nullable=False, primary_key=True)
	location_name = db.Colun(db.String(255), db.ForeignKey('location.location_name'), nullable=False)

	program = db.relationship('Program')
	location = db.relationship('Location')
