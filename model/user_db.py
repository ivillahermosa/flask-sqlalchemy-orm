# import 'db' initialized in tes_db.py file
from backend.test_db import db


class User_DB(db.Model):
    __tablename__ = 'Users'
    UserId = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(255))
    Password = db.Column(db.String(255))
    Firstname = db.Column(db.String(255))
    Middlename = db.Column(db.String(255))
    Lastname = db.Column(db.String(255))
