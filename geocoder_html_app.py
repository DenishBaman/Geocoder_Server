#!flask/bin/python
from flask import Flask, request, render_template
from geodecoder import addressToLatLng


app = Flask(__name__)

@app.route('/')
def address_querybox():
	return render_template('address_querybox-form.html')

@app.route('/', methods = ['POST'])
def address_querybox_text():
	text = request.form['text']
	result = addressToLatLng(text)
	return result.replace("\n","<br />")
	#to_render = addressToLatLng.replace("\n","<br />")
if __name__ == '__main__':
    app.run(debug=True)