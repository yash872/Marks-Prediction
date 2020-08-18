from flask import Flask, render_template, request, redirect 
from sklearn.externals import joblib

app = Flask(__name__)

model = joblib.load('model.pkl')

@app.route('/')
def hello():
	return render_template("index.html")

@app.route('/reload')
def reload():
	return redirect('/')

@app.route('/', methods=['POST'])
def marks():
	if request.method == 'POST':
		if(request.form['hours']):
			hours = float(request.form['hours'])
			marks = (model.predict([[hours]]))[0][0]
			marks = round(marks, 2)
		else:
			return render_template("index.html")

	return render_template("index.html", your_marks=marks)

if __name__ == "__main__":
	app.run(debug = True)