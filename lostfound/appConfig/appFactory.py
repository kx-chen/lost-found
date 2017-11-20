from flask import Flask
from .dbClient import db


def create_app(cfg=None):
    app = Flask('lostfound')
    app.config['SQLALCHEMY_DATABASE_URI'] =  'postgres://vxtsfazasjzswx:343e88d24e1d42804c275bcfc1dc9b58cc294ce0c47870bac43a25ca87fe8ca1@ec2-54-221-196-253.compute-1.amazonaws.com:5432/d8l24k56ov6qsv'
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    
    db.init_app(app)
    return app
