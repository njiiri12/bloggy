from flask_wtf import FlaskForm 
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField,TextAreaField,SubmitField,ValidationError
from wtforms.validators import Email,Required
from flask_login import current_user
from ..models import User

class UpdateProfile(FlaskForm):
    bio =TextAreaField('Write something about yourself',validators =[Required()])
    profile_pic = FileField('Picture', validators = [FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')


    def validate_email(self,email):
        if email.data != current_user.email:
            if User.query.filter_by(email = email.data).first():
                raise ValidationError("Invalid Email!")
    def validate_username(self,username):
        if username.data != current_user.username:
            if User.query.filter_by(username = username.data).first():
                raise ValidationError("Invalid Username")

class CreateBlog(FlaskForm):
    title = StringField('Blog Title',validators=[Required()])
    content = TextAreaField('Blog Content',validators=[Required()])
    submit = SubmitField('Post')
