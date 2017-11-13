# from werkzeug import generate_password_hash, check_password_hash
# from dbClient.client import db
# from flask_sqlalchemy import SQLAlchemy

# class User(db.Model):
#   __tablename__ = 'users'
#   uid = db.Column(db.Integer, primary_key = True)
#   firstname = db.Column(db.String(100))
#   lastname = db.Column(db.String(100))
#   email = db.Column(db.String(120), unique=True)
#   pwdhash = db.Column(db.String(120))
  
#   def __init__(self, firstname, lastname, email, password):
#     self.firstname = firstname.title()
#     self.lastname = lastname.title()
#     self.email = email.lower()
#     self.set_password(password)
     
#   def set_password(self, password):
#     self.pwdhash = generate_password_hash(password)

#   def check_password(self, password):
#     return check_password_hash(self.pwdhash, password)


# class Item(db.Model):
#     __tablename__ = 'items'
#     id = db.Column(db.Integer, primary_key= True)
#     name = db.Column(db.String(255))
#     details = db.Column(db.Text, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.uid'),
#         nullable=False)
    
#     def __init__(self, name, details, user_id):
#         self.name = firstname.title()
#         self.details = details
#         self.user_id = user_id
