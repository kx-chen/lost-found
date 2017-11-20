from flask import Flask
from .dbClient import db


def create_app(cfg=None):
    app = Flask('lostfound.app')
    return app
