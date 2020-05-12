from flask import Flask, render_template, url_for, request
import re
import functions.address as address
# <script>
#     var x;
#     function upload() {
#       var file = document.getElementById("imgInp").files;
#       if (file.length > 0) {
#         var fileReader = new FileReader();
#         fileReader.onload = function (event) {
#           document
#             .getElementById("preview")
#             .setAttribute("src", event.target.result);
#         };
#       }
#       fileReader.readAsDataURL(file[0]);
#       x = file[0].name;
#       return x;
#     }
#     console.log((x = upload()));
# </script>

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("ocr.html")

# @app.route('/ocr')
# def classify():
# 	return render_template("ocr.html")

@app.route('/ocr', methods=['POST'])
def ocr_address():
	if request.method == 'POST':
		raw_text = request.form['raw_text']
		# results = classifier.predict("model/", "image_test2/","predict.json")
		results = address.test(raw_text)
	return render_template("ocr.html", results=results,raw_text=raw_text)

if __name__ == '__main__':
	 app.run(debug=True)	
	#  app.run()	