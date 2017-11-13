from flask import Flask
app = Flask(__name__)



# Blueprints
from views.public import public_routes
from views.users import user_routes 

app.register_blueprint(public_routes.mod)
app.register_blueprint(user_routes.mod, url_prefix='/users')

