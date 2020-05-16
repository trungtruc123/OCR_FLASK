from flask import Flask, render_template, url_for, request, send_file
import re
import functions.address as address
from PIL import Image
import numpy as np
import json
import io
from tensorflow.keras.preprocessing.image import img_to_array
import cv2 
from werkzeug.utils import secure_filename
import os
path = '/home/truc/Desktop/OCR_FLASK/'
path_preview = os.path.join(path ,'image_dow')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = path_preview
@app.route('/')
def index():
	return render_template("ocr.html")
@app.route('/ocr', methods=['POST'])
def ocr_address():
	if request.method == "POST":
		image = request.files['image']
		name_img = secure_filename(image.filename)
		image = Image.open(image)
		image.save(path + 'image_dow/'+ 'pic1'+'.jpg')
		results = address.predict(path + "model/",path + "image_dow/", path +"predict.json")
		preview = os.path.join(app.config['UPLOAD_FOLDER'],'pic1.jpg')
	return render_template("ocr.html", results = results, raw_text = name_img, preview = preview)
	
	# height = 64
	# width  = 1280
	# results = 0
	# # if request.files.get("image"):
	# if request.method == 'POST':
	# 	# get name picture
	# 	#get file image :user upload
	# 	image = request.files['image'].read()
	# 	#Convert image -> array image
	# 	image =  Image.open(io.BytesIO(image))
	# 	# image = image.resize((height,width))
	# 	image = img_to_array(image)
	# 	# image = np.expand_dims(image, axis=0)
	# 	print('image:', image.shape)
	# 	# cv2.imshow('1.jpg',image)
	# 	cv2.imwrite('../image_dow/'+ str(1)+'.png', image)
		
	
	# 	# # Predict
	# 	# # results = address.predict("model/",image, "predict.json")
	# 	# results = image.shape[1]
	# 	# print( 'shape:',image.shape)
	# else:
	# 	results = 120
	# return render_template("ocr.html", results = results, raw_text = 'ngu')
if __name__ == '__main__':
	 app.run( threaded=False)	