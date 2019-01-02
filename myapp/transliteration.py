from flask import Flask, render_template, request,session
import os
from trans import converthindi, convertenglish

app = Flask(__name__)
app.secret_key = os.urandom(16)


@app.route("/", methods=['GET','POST'])
def home():
	return render_template('home.html')

@app.route("/ans", methods=['GET','POST'])
def index():
	data = request.form['trans']
	converthindi(data)
	return (render_template('ans.html', answer=converthindi(data),data=data))

@app.route("/hindi", methods=['GET','POST'])
def hindi():
	data = request.form['trans']
	convertenglish(data)
	return (render_template('hindi.html', answer=convertenglish(data), data=data))

if __name__ == "__main__":
	app.run(debug = True)