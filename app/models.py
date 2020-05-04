from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin,db.model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key= True)
    username = db.Column(db.String(255),nullable=False, unique=True)
    email = db.Column(db.String(255), nullable =False,unique=True)
    bio = db.Column(db.String(255))
    profile_img = db.Column(db.String(255))
    password_u = db.Column(db.String(255),nullable = False)
    pitches = db.relationship('Pitch', backref = 'user', lazy = 'dynamic')
    comments = db.relationship('Comment', backref = 'user', lazy = 'dynamic')

    def save_user(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_user(self):
        db.session.delete(self)
        db.session.commit()
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_u = generate_password_hash(password)
   
    def verify_password(self, password):
        return check_password_hash(self.password_u, password)
    def __repr__(self):
     return f'User {self.username}'

class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(40))
    content = db.Column(db.String)
    category = db.Column(db.String(40))
    author = db.Column(db.String(40))
    upvote = db.Column(db.Integer)
    downvote = db.Column(db.Integer)
    date_posted = db.Column(db.DateTime, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref = 'pitch', lazy = 'dynamic')
    
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()