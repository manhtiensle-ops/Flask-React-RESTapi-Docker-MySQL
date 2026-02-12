from flask import Flask, redirect, url_for

webapp = Flask(__name__)

@webapp.route('/')
def index():
    return "Test"

@webapp.route('/<name>')
def user(name):
    return f"hello {name}"

@webapp.route('/admin')
def admin():
    return redirect(url_for('user',name = 'admin!'))

webapp.run(host = "0.0.0.0", port =80)