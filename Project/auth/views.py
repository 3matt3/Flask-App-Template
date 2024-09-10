from flask import Blueprint, Flask, render_template, redirect, url_for
from flask_login import LoginManager, UserMixin, login_required, logout_user, login_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import bcrypt, generate_password_hash
from uuid import  UUID, uuid4
from . import auth
from .. import db, login_manager

#auth = Blueprint('auth', __name__)

#login_manager = LoginManager()
#login_manager.init_app(auth)

@login_manager.user_loader
def load_user(id):
   # return db.session.execute()
    return User.get_id(id)
    return User.query.get(int(id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255))
    history = db.Column(db.String(255))

class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Username"})
    
    password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Password"})
    
    email = EmailField(validators=[InputRequired(), Length(
        min = 4, max = 30)], render_kw={"placeholder": "Email"})
    
    submit = SubmitField("Register")

    #def validate_username(self, username):
    #    existing_user_username = User.query.filter_by(
    #        username=username.data).first()
        
    #    if existing_user_username:
    #        raise ValidationError(
    #            "That username already exists"
    #        )
        
class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Username"})
    
    password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Password"})
    
    submit = SubmitField("Login")


@auth.route("/login", methods=['POST', 'GET'])
def login():
    form = LoginForm()


#
#   NEED LOGIN TO WORK FFS
#
    if form.validate_on_submit():
        user = User(username=form.username.data, password=hashed_password)
        username = form.username.data
        hashed_password = generate_password_hash(form.password.data)
        users = db.session.execute(f'SELECT username FROM public.users')
        if username in users:
            if bcrypt.checkpw(form.password.data, hashed_password):
                login_user(user)
                return redirect(url_for('profile'))

    return render_template('login.html', form=form)

@auth.route('/signup', methods=['POST', 'GET'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        new_user_id = uuid4()
        new_user = User(id=new_user_id, username=form.username.data, password=hashed_password, email=form.email.data)
        
        
        db.session.execute(f"""INSERT INTO public.users(
	id, username, email, passwd, history)
	VALUES ({new_user.id}, {new_user.username}, {new_user.password}, {new_user.email});""")
        
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('signup.html', form=form)



@auth.route('/login', methods=['POST'])
def login_post():
    # code to validate to database goes here
    # Add user databs
    return redirect(url_for('auth.login'))

@login_required
@auth.route("/profile")
def profile():
    return render_template('profile.html')


@auth.route('/logout')
def logout():
    return 'Logout'

@auth.route("/admin")
def admin():
    return render_template('admin.html')