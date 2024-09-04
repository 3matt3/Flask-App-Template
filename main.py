from flask import Flask
from flask import render_template


#
#   To start test server. Be in main directory in console. In console python -m flask --app main run
#

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('base.html')

@app.route("/admin")
def admin():
    return render_template('admin.html')

@app.route("/login")
def login():
    return render_template('login.html')


