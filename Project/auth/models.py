from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import Us
db = SQLAlchemy()  # <--- The db object belonging to the root app

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255))
    history = db.Column(db.String(255))