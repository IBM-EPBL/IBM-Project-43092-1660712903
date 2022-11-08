from flask import Flask, render_template, request
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
import tensorflow as tf
import os

y_pred = 0
app = Flask(__name__)
model = load_model('E:\Github\IBM-Project-43092-1660712903\Project Development Phase\Sprint 2\models\mnistCNN.h5')

@app.route('/')
def upload_file():
    return render_template('index.html')

@app.route('/home')
def upload_file1():
    return render_template('index.html')

@app.route('/about')
def upload_file2():
    return render_template('index.html')

@app.route('/upload')
def upload_file3():
    return render_template('web.html')

@app.route('/recognize')
def upload_file4():
    return render_template('web.html')

@app.route('/predict', methods =['POST'])
def upload_image_file():
    if request.method == 'POST':
        img = Image.open(request.files['file'].stream).convert("L")
        img = img.resize((28,28))
        im2arr = np.array(img)
        im2arr = im2arr.reshape(1,28,28,1)
        y_pred = np.argmax(model.predict(im2arr), axis=-1)
        print(y_pred)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)
