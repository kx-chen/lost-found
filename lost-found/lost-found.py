from flask import Flask, render_template



app = Flask(__name__)

# Blueprints
from views.public import public_routes
from views.users import user_routes
app.register_blueprint(public_routes.mod)
