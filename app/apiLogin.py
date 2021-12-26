from flask.globals import request
from flask_cors import CORS, cross_origin
from flask import render_template, Flask
from werkzeug.utils import redirect

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['CORS_HEADERS'] = 'Content-Type'

 

@app.route("/login")
def login():			
	return render_template('login.html')

@app.route('/login', methods=['POST','GET'])
def login_post():
	email = request.form['email']
	senha = request.form['password']
	processo_email = email.upper()
	processo_senha = senha.upper()
	return processo_email

if __name__ == "__main__":
	app.run()