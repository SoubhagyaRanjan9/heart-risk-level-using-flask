from flask import Flask,render_template
app=Flask(__name__)


@app.route('/')
def index():

	return 'Hello This is my Website'

@app.route('/page1')
def page1():

	return 'This is my First Page'

@app.route('/page2')
def page2():

	return render_template('page2.html')

app.run(debug=True)
