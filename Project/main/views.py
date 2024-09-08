from flask import Flask, Blueprint
from flask import render_template, redirect, url_for, request
from . import main

#main = Blueprint('main', __name__, template_folder="templates", static_folder="static")

@main.route("/", methods=['GET', 'POST'])
def landing():
    return render_template('home.html')

@main.route("/home")
def home():
    return render_template('home.html')


@main.route("/about")
def about():
    return render_template('about.html')

@main.route("/profile")
def profile():
    return render_template('profile.html')
