# app/models.py

from app import db

class Student(db.Model):
        __tablename__ = 'student'
        student_email = db.Column(db.String(255), primary_key=True, unique=True, nullable=False)
        major = db.Column(db.String(100), nullable=False)
        primary_reason = db.Column(db.String(255), nullable=False)
        language_proficiency = db.Column(db.String(50), nullable=False)
