from flask import Flask
from dbClient.client import db
from flask_login import LoginManager, login_user, login_required, logout_user
from dbClient.client import login_manager
import config

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']
app.secret_key = os.environ['SECRET_KEY']
db.init_app(app)

login_manager.init_app(app)


# Blueprints
from public import public_views
from users import user_views
from items import item_views

app.register_blueprint(public_views.mod)
app.register_blueprint(user_views.mod, url_prefix='/users')
app.register_blueprint(item_views.mod, url_prefix='/items')