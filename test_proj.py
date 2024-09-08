from Project import create_app, main, auth

app = create_app()


app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as app_blueprint
    app.register_blueprint(app_blueprint)