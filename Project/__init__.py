from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    #db = SQLAlchemy()
    app = Flask(__name__, static_folder=None)

    app.config['SECRET_KEY'] = '333mmm333mmm3m3m3m'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:merlayn313@localhost:5432/SubstanceSecrets'

    db.init_app(app)

    
    login_manager.init_app(app)
    

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as app_blueprint
    app.register_blueprint(app_blueprint)


    return app

