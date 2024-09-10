from flask import Flask, Blueprint

auth = Blueprint('auth', __name__,
                template_folder='templates',
                static_folder='./static')


from . import views
