# app/models.py

#from app import db
# from sqlalchemy.engine import URL
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
        __tablename__ = 'student'
        student_email = Column(String(255), nullable=False, primary_key=True)
        primary_reason = Column(Text())

class Major(db.Model):
	__tablename__ = 'major'
	major_name = Column(String(255), nullable=False, primary_key=True)

class Has_Major(db.Model):
	__tablename__ = 'has_major'
	student_email = Column(String(255), ForeignKey('student.student_email'), nullable=False, primary_key=True)
	major_name = Column(String(255), ForeignKey('major.major_name'), nullable=True, primary_key=True)

	student = relationship('Student')
	major = relationship('Major')
#question for Prof. Riondato: include a backref here?

class Program(db.Model):
	__tablename__ = 'program'
	program_name = Column(String(255), nullable=False, primary_key=True)

class Term(db.Model):
	__tablename__ = 'term'
	term_id = Column(String(255), nullable=False, primary_key=True)

class Participates_In(db.Model):
	__tablename__ = 'participates_in'
	student_email = Column(String(255), ForeignKey('student.student_email'), nullable=False, primary_key=True)
	program_name = Column(String(255), ForeignKey('program.program_name'), nullable=False, primary_key=True)
	term_id = Column(String(255), ForeignKey('term.term_id'), nullable=False, primary_key=True)

	student = relationship('Student')
	program = relationship('Program')
	term = relationship('Term')


class Personal_Reflection(db.Model):
	__tablename__ = 'personal_reflection'
	student_email = Column(String(255), ForeignKey('student.student_email'), nullable=False, primary_key=True)
	program_name = Column(String(255), ForeignKey('program.program_name'), nullable=False, primary_key=True)
	term_id = Column(String(255), ForeignKey('term.term_id'), nullable=False, primary_key=True)
	pr_id = Column(String(255), nullable=False, primary_key=True)
	goals_reflection = Column(Text())
	growth = Column(Text())
	challenges = Column(Text())
	new_perspectives = Column(Text())
	language_proficiency_before = Column(Text())
	language_proficiency_after = Column(Text())

	student = relationship('Student')
	program = relationship('Program')
	term = relationship('Term')


class Program_Reflection(db.Model):
	__tablename__ = 'program_reflection'
	student_email = Column(String(255), ForeignKey('student.student_email'), nullable=False, primary_key=True)
	program_name = Column(String(255), ForeignKey('program.program_name'), nullable=False, primary_key=True)
	term_id = Column(String(255), ForeignKey('term.term_id'), nullable=False, primary_key=True)
	pgr_id = Column(String(255), unique=True, primary_key=True)
	recommendation_rating = Column(Text())
	recommendation_comments = Column(Text())

	student = relationship('Student')
	program = relationship('Program')
	term = relationship('Term')

class Is_About_Academic_Factors(db.Model):
	__tablename__ = 'is_about_academic_factors'
	pgr_id = Column(db.String(255), ForeignKey('program_reflection.pgr_id'), nullable=False, primary_key=True)
	program_name = Column(db.String(255), ForeignKey('program.program_name'), nullable=False)
	term_id = Column(db.String(255), ForeignKey('term.term_id'), nullable=False)
	courses_taken = Column(Text())
	courses_type = Column(Text())
	academic_exc_avail = Column(Text())
	academic_exc_rating = Column(Text())
	academic_exc_comments = Column(Text())
	influencing_factors = Column(Text())
	orientation_description = Column(Text())

	program_reflection = relationship('Program_Reflection')
	program = relationship('Program')
	term = relationship('Term')


class Is_About_Financial_Factors(db.Model):
	__tablename__ = 'is_about_financial_factors'
	pgr_id = Column(db.String(255), ForeignKey('program_reflection.pgr_id'), nullable=False, primary_key=True)
	program_name = Column(db.String(255), ForeignKey('program.program_name'), nullable=False)
	term_id = Column(db.String(255), ForeignKey('term.term_id'), nullable=False)
	amount_spent = Column(db.String(255))
	city_affordability = Column(Text())
	housing_acc = Column(Text())
	housing_acc_comments = Column(Text())

	program_reflection = relationship('Program_Reflection')
	program = relationship('Program')
	term = relationship('Term')

class Is_About_Social_Factors(db.Model):
	__tablename__ = 'is_about_social_factors'
	pgr_id = Column(db.String(255), ForeignKey('program_reflection.pgr_id'), nullable=False, primary_key=True)
	program_name = Column(db.String(255), ForeignKey('program.program_name'), nullable=False)
	term_id = Column(db.String(255), ForeignKey('term.term_id'), nullable=False)
	extracurriculars = Column(Text())
	attitudes_diff = Column(Text())
	attitudes_diff_comments = Column(Text())
	res_staff = Column(Text())
	res_staff_comments = Column(Text())
	leisure_exc_avail = Column(Text())
	leisure_exc_rating = Column(Text())
	leisure_exc_comments = Column(Text())

	program_reflection = relationship('Program_Reflection')
	program = relationship('Program')
	term = relationship('Term')

class Location(db.Model):
	__tablename__ = 'location'
	location_name = Column(db.String(255), nullable=False, primary_key=True)
	primary_lang_spoken = Column(db.String(255))
	country = Column(db.String(255))

class Hosted_In(db.Model):
	__tablename__ = 'hosted_in'
	program_name = Column(db.String(255), ForeignKey('program.program_name'), nullable=False, primary_key=True)
	location_name = Column(db.String(255), ForeignKey('location.location_name'), nullable=False)

	program = relationship('Program')
	location = relationship('Location')
