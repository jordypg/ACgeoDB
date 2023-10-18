from flask import Flask

api = Flask(__name__)

@api.route('/profile')
def my_profile():
    response_body = {
        "name": "GEO",
        "about" :"GEO DB Project"
    }

    return response_body