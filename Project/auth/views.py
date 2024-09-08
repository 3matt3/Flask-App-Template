from flask import Blueprint, render_template, redirect, url_for
from . import auth

#auth = Blueprint('auth', __name__)

@auth.route("/login")
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    # code to validate and add user to database goes here
    return redirect(url_for('auth.login'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/logout')
def logout():
    return 'Logout'

@auth.route("/admin")
def admin():
    return render_template('admin.html')