from flask import render_template,flash,redirect,url_for
from app import app,db
from .forms import LoginForm
from flask_login import current_user,login_user,login_required,logout_user
from app.models import User
from app.forms import RegistrationForm

@app.route('/')
@app.route('/index')
@login_required
def index():
	return render_template('index.html',title='Home')

@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form=LoginForm()
   # print '''rememberme data %d,lable=%s\n''' %(form.remember_me.data,form.remember_me.label)
    if form.validate_on_submit():
        flash('Login requested for user {},remember_me={}'.format(form.username.data,form.remember_me.data))
        user=User.query.filter_by(username=form.username.data).first()
        print user
        print user.password_hash
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        print  'redirect to index'
        login_user(user,remember=form.remember_me.data)
        return redirect(url_for('index'))
    print 'render_template login.html'
    return render_template('login.html',title='Sign In',form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)    
