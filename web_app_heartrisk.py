from flask import Flask,render_template,request



app= Flask(__name__)

@app.route('/')
def index():

	return render_template('home.html')

@app.route('/getresults',methods=['POST'])
def getresults():

	form_data= request.form

    print(form_data)

    return render_template('home.html')
app.run(debug=True)