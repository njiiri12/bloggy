from flask import redirect,render_template,url_for,request,flash
from app.auth import auth
from app.models import User
from .forms import RegistrationForm,LoginForm
from flask_login import login_user,login_required,logout_user
from ..email import mail_message



@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email = form.email.data, password = form.password.data )
        user.save_user()
        # mail_message('Welcome to MyBlog','email/welcome',user.email,user=user)
        return redirect(url_for('auth.login'))
    return render_template('auth/sign_up.html',registration_form=form)


@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "MyBlogLogin"
    return render_template('auth/sign_in.html',login_form = login_form,title=title)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))