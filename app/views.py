from flask import render_template,flash,redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user={'nickname':'Miguel'} #only fake user
	posts=[
	{
		'author':{'nickname':'John'},
		'body':'beautiful day in Portland!'
	},
	{
		'author':{'nickname':'Susan'},
		'body':'the Avengers movie was so cool!'
	}
	]
	return render_template('index.html',title='Home',user=user,posts=posts)

@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
   # print '''rememberme data %d,lable=%s\n''' %(form.remember_me.data,form.remember_me.label)
    if form.validate_on_submit():
        flash('Login requested for user {},remember_me={}'.format(form.username.data,form.remember_me.data))
        print  'redirect to index'
        return redirect('/index')
    print 'render_template login.html'
    return render_template('login.html',title='Sign In',form=form)
