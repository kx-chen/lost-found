from flask import Blueprint, render_template, abort, session, redirect, url_for
from jinja2 import TemplateNotFound
from flask_login import current_user
from lostfound.appConfig.helpers import logged_out_required

mod = Blueprint('public_views', __name__)

@mod.route('/')
@logged_out_required("item_views.dashboard")
def index():
	return render_template('public/index.html')

@mod.route('/about')
def about():
	return render_template('public/about.html')

@mod.route('/contact')
def contact():
	return render_template('public/contact.html')

