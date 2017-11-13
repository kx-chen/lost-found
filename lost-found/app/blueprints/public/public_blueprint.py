from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

public_routes = Blueprint('public_routes', __name__)

@public_routes.route('/')
def show():
	return render_template('public/index.html')

@public_routes.route('/about'):
def about():
	return render_template('public/about.html')

@public_routes.route('/contact'):
def contact():
	return render_template('public/contact.html')

