from flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound
from .models import User
from dbClient.client import db

from dbClient.client import login_manager
from flask_login import LoginManager, login_user, login_required, logout_user
from .forms import SignupForm

mod = Blueprint('user_views', __name__)

@mod.route('/')
def error():
	abort(404)

@mod.route('/register', methods=['GET', 'POST'])
def register():
	form = SignupForm()
	if request.method == 'GET':
		return render_template('users/register.html', form=form)
	elif request.method == 'POST':
		if form.validate_on_submit():
			if User.query.filter_by(email=form.email.data).first():
				# flash email already exists message
				return render_template('users/register.html', form = form)
			else:
				newuser = User(form.email.data, form.password.data)
				db.session.add(newuser)
				db.session.commit()
				login_user(newuser)
				# flash accoutn created
				return render_template('users/dashboard.html')
	else:
		# error in making account
		return render_template('users/register.html', form=form)

@mod.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
	return render_template('users/sign_in.html')

