from werkzeug import generate_password_hash, check_password_hash
from appConfig.dbClient import db
from flask_sqlalchemy import SQLAlchemy

class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(255))
    details = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
        nullable=False)
    
    def __init__(self, name, details, user_id):
        self.name = name.title()
        self.details = details
        self.user_id = user_id
        