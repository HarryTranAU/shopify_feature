from main import db                                                                   
from models.Store import Store                                                    
from sqlalchemy.orm import backref                                                    

class User(db.Model):                                                                 
    __tablename__= "users"                                                            

    id = db.Column(db.Integer, primary_key=True)                                      
    email = db.Column(db.String(), nullable=False, unique=True)                       
    password = db.Column(db.String(), nullable=False)                                 
    store = db.relationship("Store", backref=backref("user", uselist=False))      

    def __repr__(self):                                                               
        return f"<User {self.email}>"