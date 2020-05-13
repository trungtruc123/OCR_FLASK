from flask import Flask, render_template, url_for, request
import re
import functions.address as address
app = Flask(__name__)

@app.route('/')
def index():
	return render_template("ocr.html")
def ocr_address():
	raw_text = request.form['raw_text']
	results = classifier.predict("model/", "image_test2/","predict.json")
	results = address.test(raw_text)
	return render_template("ocr.html", results=results,raw_text=raw_text)
# @app.route('/ocr')
# def classify():
# 	return render_template("ocr.html")

# @app.route('/ocr', methods=['POST'])
# # def ocr_address():
# # 	if request.method == 'POST':
# # 		raw_text = request.form['raw_text']
# # 		results = classifier.predict("model/", "image_test2/","predict.json")
# # 		results = address.test(raw_text)
# # 	return render_template("ocr.html", results=results,raw_text=raw_text)
# def ocr_address():
# 	if request.method == 'POST':
# 		results = address.predict("model/", "image_test2/","predict.json")
# 		return render_template('ocr.html',results = 'ngu', raw_text ='truc')
# 	elif request.method == 'GET':
# 		results = address.predict("model/", "image_test2/","predict.json")
# 		return render_template('ocr.html',results = 'ngu', raw_text ='truc')

if __name__ == '__main__':
	 app.run(debug=True)	
	#  app.run()	