from flask import Flask
from .dbClient import db

from lostfound.public import public_views
from lostfound.users import user_views
from lostfound.items import item_views
from flask_sqlalchemy import SQLAlchemy

def create_app(cfg=None):
    app = Flask('lostfound')
    db.app = app
    db.init_app(app)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] =  'postgres://vxtsfazasjzswx:343e88d24e1d42804c275bcfc1dc9b58cc294ce0c47870bac43a25ca87fe8ca1@ec2-54-221-196-253.compute-1.amazonaws.com:5432/d8l24k56ov6qsv'
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    
    app.register_blueprint(public_views.mod)
    app.register_blueprint(user_views.mod, url_prefix='/users')
    app.register_blueprint(item_views.mod, url_prefix='/items')
    
    
    
    return app
