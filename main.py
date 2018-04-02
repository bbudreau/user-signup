from flask import Flask, request, redirect, render_template
import cgi
import os


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('user_form.html')

@app.route("/valdiate-form", methods=['POST'])
def validate_form():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    email_error = ''
    
    if username > 20 or username <3:
        username_error = "username not valid"
        username = ''
    if password > 20 or password <3:
        password_error = "password is not valid"
        password = ''
    
    





app.run()
