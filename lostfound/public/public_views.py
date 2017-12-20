from flask import Blueprint, render_template, abort, session, redirect, url_for
from jinja2 import TemplateNotFound
from flask_login import current_user

mod = Blueprint('public_views', __name__)

@mod.route('/')
def index():
	if current_user.is_authenticated:
		return redirect(url_for("item_views.dashboard"))
	else:
		return render_template('public/index.html')

@mod.route('/about')
def about():
	return render_template('public/about.html')

@mod.route('/contact')
def contact():
	return render_template('public/contact.html')

