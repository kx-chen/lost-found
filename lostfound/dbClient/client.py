from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user

login_manager = LoginManager()
db = SQLAlchemy()