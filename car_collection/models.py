from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
from datetime import datetime

from werkzeug.security import check_password_hash, generate_password_hash

import secrets

db = SQLAlchemy()

class Person(db.Model):
    id = db.Column(db.String, primary_key = True)
    first_name = db.Column(db.String(150), nullable = True, default = "")
    last_name = db.Column(db.String(150), nullable = True, default= "")
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String, nullable = True, default = "")
    token = db.Column(db.String, default = "", unique = True)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    favorite_car = db.Column(db.String(150), nullable = True, default="")
    
    def __init__(self,email, first_name ="", last_name = "",password ="", token = "",favorite_car=""):
        self.id = self.get_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.get_password(password)
        self.email = email
        self.token = self.get_token(24)
        self.favorite_car = favorite_car
                
    def get_token(self,number):
        return secrets.token_hex(number)
    def get_id(self):
        return str(uuid.uuid4())
        
    def get_password(self,pw):
        self.pw_hash = generate_password_hash(pw)
        return self.pw_hash
    
    def __repr__(self):
        return f"User {self.email} added to db!"
    
    