from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:geodb@localhost/project'
db = SQLAlchemy(app)


class Student(db.Model):
	__tablename__ = 'student'
	student_email = db.Column(db.String(255), primary_key=True, unique=True, nullable=False)
	major = db.Column(db.String(100), nullable=False)
	primary_reason = db.Column(db.String(255), nullable=False)
	language_proficiency = db.Column(db.String(50), nullable=False)

@app.route('/')
def index():
	first_student = Student.query.first()
	return f'Student email: {first_student.student_email}'
if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
