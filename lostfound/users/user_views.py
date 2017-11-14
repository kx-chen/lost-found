from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from .models import User
from dbClient.client import db

from dbClient.client import login_manager
from flask_login import LoginManager, login_user, login_required, logout_user

mod = Blueprint('user_views', __name__)

@mod.route('/')
def error():
	abort(404)

@mod.route('/register', methods=['GET', 'POST'])
def register():
	return render_template('users/register.html')

@mod.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
	return render_template('users/sign_in.html')

