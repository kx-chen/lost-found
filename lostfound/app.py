from flask import Flask
from appConfig.dbClient import db
from appConfig.appFactory import create_app

app = create_app()
app.config['SQLALCHEMY_DATABASE_URI'] =  'postgres://vxtsfazasjzswx:343e88d24e1d42804c275bcfc1dc9b58cc294ce0c47870bac43a25ca87fe8ca1@ec2-54-221-196-253.compute-1.amazonaws.com:5432/d8l24k56ov6qsv'
# psql -h localhost -U kai postgres
# flask run -h 0.0.0.0 -p 8080

# 'postgresql://kai:opensesame@localhost:5432/postgres'
#'postgres://vxtsfazasjzswx:343e88d24e1d42804c275bcfc1dc9b58cc294ce0c47870bac43a25ca87fe8ca1@ec2-54-221-196-253.compute-1.amazonaws.com:5432/d8l24k56ov6qsv'
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
db.init_app(app)

# login_manager.init_app(app)


# Blueprints
from public import public_views
from users import user_views
from items import item_views

app.register_blueprint(public_views.mod)
app.register_blueprint(user_views.mod, url_prefix='/users')
app.register_blueprint(item_views.mod, url_prefix='/items')
