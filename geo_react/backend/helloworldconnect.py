from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return f'I have connected successfully!'

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
