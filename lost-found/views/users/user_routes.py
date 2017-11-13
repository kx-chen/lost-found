from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

mod = Blueprint('user_routes', __name__)

@mod.route('/')
def error():
	abort(404)

@mod.route('/register')
def register():
	return render_template('users/register.html')

@mod.route('/sign_in')
def sign_in():
	return render_template('users/sign_in.html')

