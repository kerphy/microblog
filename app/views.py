from app import app
from flask import render_template
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

