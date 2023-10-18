from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# PostgreSQL configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jordypg:jordyrules@jperrygreene23@cosc-257-node14.cs.amherst.edu/project'

db = SQLAlchemy(app)

api = Flask(__name__)

@app.route('/')
def index():
    # Test a simple database query
    result = db.engine.execute('SELECT 1')
    return f"Database connection successful: {result.scalar()}"


@api.route('/profile')
def my_profile():
    response_body = {
        "name": "GEO",
        "about" :"GEO DB Project"
    }

    return response_body
