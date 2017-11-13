from flask import Flask, render_template
from app.blueprints.public.public_blueprint import public_routes


app = Flask(__name__)

app.register_blueprint(public_routes)
