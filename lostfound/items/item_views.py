from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from .models import Item
from dbClient.client import db

mod = Blueprint('item_views', __name__)

@mod.route('/')
# @login_required
def dashboard():
	return render_template('items/dashboard.html')

@mod.route('/register')
def register():
	return render_template('items/register.html')

# @mod.route('/sign_in')
# def sign_in():
# 	return render_template('users/sign_in.html')

