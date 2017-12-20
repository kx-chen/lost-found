from flask import Blueprint, render_template, abort, session, redirect, url_for, request
from jinja2 import TemplateNotFound
from flask_login import LoginManager, login_user, login_required, logout_user

from .models import Item
from lostfound.users.models import User
from .item_forms import NewItemForm
from lostfound.appConfig.dbClient import db


mod = Blueprint('item_views', __name__)

@mod.route('/<int:item_id>')
def viewItem(item_id):
	item = Item.query.get(item_id)
	
	if item: 
		userId = item.user_id
		userOwnerOfItem = User.query.get(userId)
		return render_template("items/view.html", item=item, user=userOwnerOfItem)
	else: 
		return abort(404)
	
	
@mod.route('/')
@login_required
def dashboard():
		items = Item.query.filter_by(user_id=session["user_id"])
		return render_template("items/dashboard.html", items=items)

@mod.route('/new', methods=["GET", "POST"])
def new():
	
	if 'email' not in session:
		return redirect(url_for("user_views.sign_in"))
		
	form = NewItemForm()
	
	if request.method == 'GET':
		return render_template('items/new.html', form=form)
		
	if request.method == 'POST':
		name = form.name.data
		details = form.details.data
		
		item = Item(name, details, session['user_id'])
		db.session.add(item)
		db.session.commit()
		
		return redirect(url_for("item_views.dashboard"))

# @mod.route('/sign_in')
# def sign_in():
# 	return render_template('users/sign_in.html')

