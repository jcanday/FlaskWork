from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
from datetime import datetime

from werkzeug.security import check_password_hash, generate_password_hash

import secrets

from flask_login import UserMixin, LoginManager

from flask_marshmallow import Marshmallow
db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key = True)
    first_name = db.Column(db.String(150), nullable = True, default = "")
    last_name = db.Column(db.String(150), nullable = True, default= "")
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String, nullable = True, default = "")
    token = db.Column(db.String, default = "", unique = True)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    g_auth_verify = db.Column(db.Boolean, default = False)
    
    def __init__(self,email, first_name ="", last_name = "", password = "", token = "", g_auth_verify = False):
        self.id = self.get_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.get_password(password)
        self.email = email
        self.token = self.get_token(24)
        self.g_auth_verify = g_auth_verify
                
    def get_token(self,number):
        return secrets.token_hex(number)
    def get_id(self):
        return str(uuid.uuid4())
        
    def get_password(self,password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash
    
    def __repr__(self):
        return f"User {self.email} added to db!"
    
    
class Car(db.Model):
    id = db.Column(db.String, primary_key = True)
    name = db.Column(db.String(150))
    make = db.Column(db.String(100))
    model = db.Column(db.String(100))
    year = db.Column(db.Integer())
    # user_token = db.Column(db.String, db.ForeignKey('User.token'))
    
    def __init__(self,name,make,model,year):
        self.id = self.get_id()
        self.name = name
        self.make = make
        self.model = model
        self.year = year
        # self.user_token = user_token
        
    def __repr__(self):
        return f"The following car has been added {self.name}"
    
    def get_id(self):
        return(secrets.token_urlsafe())
    
class CarSchema(ma.Schema):
    class Meta: 
        fields = ['id','name','make','model','year']

car_schema = CarSchema()
cars_schema = CarSchema(many = True)
    