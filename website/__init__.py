from flask import Flask

def create_app():
    app = Flask(__name__)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    # from .models import User

    # create_database(app)

    # login_manager = LoginManager()
    # login_manager.login_view = "auth.login"
    # login_manager.init_app(app)

    # @login_manager.user_loader
    # def load_user(id):
    #     return User.query.get(int(id))

    return app