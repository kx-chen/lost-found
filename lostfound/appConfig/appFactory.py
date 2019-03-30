from flask import Flask
from .dbClient import db

import os

from lostfound.public import public_views
from lostfound.users import user_views
from lostfound.items import item_views
from lostfound import config


def create_app(cfg=None):
    app = Flask('lostfound')

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] =  os.environ.get('DATABASE_URL', config.SQLALCHEMY_DATABASE_URI)
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    
    db.init_app(app)
    
    app.register_blueprint(public_views.mod)
    app.register_blueprint(user_views.mod, url_prefix='/users')
    app.register_blueprint(item_views.mod, url_prefix='/items')
    
    
    
    return app
