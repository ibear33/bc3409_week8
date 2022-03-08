# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 09:49:00 2022

@author: Soph
"""

from flask import Flask
from flask import request,render_template
from werkzeug.utils import secure_filename
import speech_recognition as sr

app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        print(file)
        filename = secure_filename(file.filename) #file name put into directory called static - any file inside
        print(filename)
        file.save("static/" + filename)
        a = sr.AudioFile("static/" + filename)
        with a as source:
            a = sr.Recognizer().record(source)
        s = sr.Recognizer().recognize_google(a)
        return(render_template("index.html", result=s))
    else:
        return(render_template("index.html", result = 2))
        
        
if __name__ == "__main__":
    app.run()