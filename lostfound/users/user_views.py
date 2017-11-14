from flask import Blueprint, render_template, abort, request, redirect, url_for, session
from jinja2 import TemplateNotFound
from .models import User
from dbClient.client import db

from dbClient.client import login_manager
from flask_login import LoginManager, login_user, login_required, logout_user
from .forms import SignupForm, SigninForm

mod = Blueprint('user_views', __name__)

@mod.route('/')
def index():
	if 'email' in session:
		return redirect(url_for("item_views.dashboard"))

@mod.route('/register', methods=['GET', 'POST'])
def register():
	if 'email' in session:
		return redirect(url_for("item_views.dashboard"))

	form = SignupForm()
	if request.method == 'GET':
		return render_template('users/register.html', form=form)
	elif request.method == 'POST':
		if form.validate_on_submit():
			if User.query.filter_by(email=form.email.data).first():
				# flash email already exists message
				return render_template('users/register.html', form = form)
			else:
				newuser = User(form.firstname.data, form.lastname.data, form.email.data, form.password.data)
				db.session.add(newuser)
				db.session.commit()

				session['email'] = newuser.email
				# flash accoutn created
				return redirect(url_for("item_views.dashboard"))
	else:
		# error in making account
		return render_template('users/register.html', form=form)

@mod.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
	if 'email' in session:
		return redirect(url_for('item_views.dashboard'))
	
	form = SigninForm()
	if request.method == 'POST':
		email = form.email.data
		password = form.password.data
		user = User.query.filter_by(email=email).first()

		if user is not None and user.check_password(password):
			session['email'] = email
			return redirect(url_for('item_views.dashboard'))
		else: 
			return redirect(url_for('user_views.sign_in'))
			
	elif request.method == 'GET':
		return render_template("users/sign_in.html", form=form)


@mod.route("/logout")
def logout():
    session.pop("email", None)
    return redirect(url_for("public_views.index"))



@login_manager.user_loader
def load_user(email):
    return User.query.filter_by(email = email).first()

