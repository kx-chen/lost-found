from flask import Blueprint, render_template, abort, session, redirect, url_for
from jinja2 import TemplateNotFound
from .models import Item
from dbClient.client import db
from flask_login import LoginManager, login_user, login_required, logout_user

mod = Blueprint('item_views', __name__)

@mod.route('/')
def dashboard():
	if 'email' in session:
		return render_template("items/dashboard.html")
	else: 
		return redirect(url_for("user_views.sign_in"))

@mod.route('/register')
def register():
	return render_template('items/register.html')

# @mod.route('/sign_in')
# def sign_in():
# 	return render_template('users/sign_in.html')

