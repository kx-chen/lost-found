from dbClient.client import db
# from dbClient.client import login_manager
from flask import Flask
from flask_login import LoginManager, login_user, login_required, logout_user


# import config

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] =  'postgresql://postgres:opensesame@localhost/postgres'
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
db.init_app(app)

# login_manager.init_app(app)


# Blueprints
from public import public_views
from users import user_views
from items import item_views

app.register_blueprint(public_views.mod)
app.register_blueprint(user_views.mod, url_prefix='/users')
app.register_blueprint(item_views.mod, url_prefix='/items')