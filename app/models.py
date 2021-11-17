from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime

from . import login_manager




class User(db.Model,UserMixin):
    
    __tablename__ = 'users'

    id =db.Column(db.Integer,primary_key =True)
    username = db.Column(db.String(255),unique=True,nullable=False)
    email = db.Column(db.String(255),unique=True,nullable=False)
    bio  = db.Column(db.String(255),default='My Bio')
    profile_pic_path = db.Column(db.String(255),default='blog.png')
    password_hash = db.Column(db.String(255),nullable=False)
    blog = db.relationship('Blog',backref='user',lazy='dynamic')
    comment = db.relationship('Comment',backref='user',lazy='dynamic')

    @property
    def set_password(self):
        raise AttributeError('You cannot read the password attribute')

    @set_password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def delete_user(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return "User: %s " %str(self.username)

class Blog(db.Model):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer,primary_key = True)
    title =  db.Column(db.String(255),nullable = False)
    content = db.Column(db.Text(),nullable = False)
    posted = db.Column(db.DateTime,default = datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comment = db.relationship('Comment',backref='blog',lazy='dynamic')

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    def delete_blog(self):
        db.session.add(self)
        db.session.commit()

    
    def get_blog(self,id):
        blog = Blog.query.filter_by(id=id).first()
        return blog

    def __repr__(self):
        return f'Blog {self.title}'

class Comment(db.Model):

    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key =True)
    comment = db.Column(db.String(255))
    posted = db.Column(db.DateTime,default = datetime.utcnow)
    blog_id = db.Column(db.Integer,db.ForeignKey("blogs.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))


    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    def delete_commit(self):
        db.session.add(self)
        db.session.commit()

    def get_comment(self,id):
        comment = Comment.query.all(id=id)
        return comment

    def __repr__(self):
        return f'Comment {self.comment}'

class Subscriber(db.Model):
    __tablename__='subscribers'

    id=db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(255),unique=True,index=True)

    def save_subscriber(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Subscriber {self.email}'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))