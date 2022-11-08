from flask import Flask, render_template, request
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
import tensorflow as tf

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8000,debug=True)
