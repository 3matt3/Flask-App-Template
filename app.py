from flask import Flask
from flask import render_template
import psycopg2


#
#   To start test server. Be in main directory in console. In console python -m flask --app main run
#

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/admin")
def admin():
    return render_template('admin.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/profile")
def profile():
    return render_template('profile.html')

