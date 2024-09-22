from flask import Flask, Blueprint
from flask import render_template, redirect, url_for, request
import psycopg2
from uuid import UUID, uuid4


#   To start test server. Be in main directory in console. While in the virtualenv (.venv), type 'flask run'

#app = Flask(__name__)

main = Blueprint('main', __name__)


@main.route("/")
def landing():
    return redirect(url_for("home"))

@main.route("/home", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if(request.form['submit-txt'] == ""):
            return render_template('home.html')
        else:
            text = request.form['submit-txt']
            return render_template("home.html", text=text)


    return render_template('home.html')


@main.route("/about")
def about():
    return render_template('about.html')

@main.route("/profile")
def profile():
    return render_template('profile.html')




#<input type="submit" id="submit-btn" value="" >

if __name__ == '__app__':
    main.run(host='0.0.0.0', port=5333, debug=True)


#   //  Connect to PostgreSQL DB
conn = psycopg2.connect(host="localhost", dbname="SubstanceSecrets", user="postgres", password="merlayn313", port="5432")

cur = conn.cursor()

#   //  Database CRUD Functions

def insertUser(name,emails,passwd, usage):
    """Inserts a new user into the PostgreSQL database"""
    cur = conn.cursor()
    id = '3'    # NEED TO MAKE INCREMENTING NEW ID OR UUID
    username = name
    email = emails
    password = passwd
    history = usage

    cur.execute(f"""INSERT INTO users
    VALUES ('{id}', '{username}', '{email}', '{password}', '{history}')""")

    conn.commit()
    cur.close()
    conn.close()

def insertUsage (username, drugs, dose, roa):
    cur = conn.cursor()
    id = '1'
    user = username
    drug = drugs
    dosage = dose
    route = roa

    cur.execute(f"""INSERT INTO history
                VALUES ('{id}', '{user}', '{drug}', '{dosage}', '{route}');""")
    
    conn.commit()
    cur.close()
    conn.close()










#
#   //  Need to fix getting history
#def get_history(uid, user):
#Need to fetch history data for specific user

 #   id = uid
#    username = user

#       ???
    #x = cur.execute(f"""SELECT DISTINCT
    #                {user} FROM users;""")
    
 #   y = str(cur.fetchall())

#    print(y)
#    conn.commit()
 #   cur.close()
 #   conn.close()

#get_history('1', 'matt')





#insertUser('matt','m.medwin@icloud.com', 'password333', '')
#insertUsage('matt', 'bromazolam', '8.5mg', 'Oral')