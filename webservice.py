import os
from flask import Flask
from flask import request
# -*- coding: utf-8 -*-
app = Flask(__name__)

@app.route('/')
def hello():
    return ("Hello World!!!")
@app.route('/upload_file',methods = ['POST'])
def upload_csv_file():
    if request.method == 'POST':
        print(request.files['file'])
        file = request.files['file']
        ten_file = file.filename
        if file:
            file.save("Data_Uploaded/"+ten_file)
    return "method:POST"
if __name__ == "__main__":
    app.run(host = "192.168.1.32",port = 2905,debug = True)