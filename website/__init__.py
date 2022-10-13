from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config['SECRET KEY'] = 'b49864935690f007c2e4e90da26ad00f'
    
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
