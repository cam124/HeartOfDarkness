from flask import Flask

def create_app():
    thisapp = Flask(__name__)
    thisapp.config['SECRET_KEY'] = 'ThisIsMySecretKey'

    from .views import views

    thisapp.register_blueprint(views, url_prefix='/')

    return thisapp

myapp = create_app()