from flask import Blueprint, render_template, abort, request, redirect, url_for, session, flash
from jinja2 import TemplateNotFound
from .models import User
from appConfig.dbClient import db

# from app.client import login_manager
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
		
		if form.validate():
			if User.query.filter_by(email=form.email.data).first():
				flash("Email already exists, please use another email.", 'warning')
				return render_template('users/register.html', form = form)
			else:
				newuser = User(form.firstname.data, form.lastname.data, form.email.data, form.password.data)
				db.session.add(newuser)
				db.session.commit()

				session['email'] = newuser.email
				session["user_id"] = newuser.id
				flash("Account created, you are now logged in.", 'success')
				return redirect(url_for("item_views.dashboard"))
		else:
			# error has occured
			for field, errors in form.errors.items():
				for error in errors:
					flash(u"Error in the %s field - %s" % (getattr(form, field).label.text,error), "warning")
			return render_template('users/register.html', form=form)

@mod.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
	if 'email' in session:
		flash("You are already signed in.", 'success')
		return redirect(url_for('item_views.dashboard'))
	
	form = SigninForm()
	if request.method == 'POST':
		email = form.email.data
		password = form.password.data
		user = User.query.filter_by(email=email).first()

		if user is not None and user.check_password(password):
			session['email'] = email
			session['user_id'] = user.id
			flash("Logged in successfully.", 'success')
			return redirect(url_for('item_views.dashboard'))
		else: 
			flash("Incorrect username or password. Please try again.", 'success')
			return redirect(url_for('user_views.sign_in'))
			
	elif request.method == 'GET':
		return render_template("users/sign_in.html", form=form)


@mod.route("/logout")
def logout():
	flash("Logged out.", 'success')
	session.pop("email", None)
	return redirect(url_for("public_views.index"))
	