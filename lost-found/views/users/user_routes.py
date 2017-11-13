from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

mod = Blueprint('user_routes', __name__)

# @mod.route('/')
# def show():
# 	return render_template('public/index.html')

# @mod.route('/about')
# def about():
# 	return render_template('public/about.html')

# @mod.route('/contact')
# def contact():
# 	return render_template('public/contact.html')

