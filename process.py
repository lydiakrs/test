from tkinter import image_names
from turtle import width
import matplotlib as plt
import keras as kr
import sounddevice as sd

from flask import Flask, render_template,request,Response
import cv2,imutils,time
import pyshine as ps
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

def pyshine_process(params):
    cam = cv2.VideoCapture(0)

    cpt = 0

    while True:
        check, frame = cam.read()
        cv2.imshow('video', frame)
        key = cv2.waitKey(1)

        if key == 27:
            cam.release()
            cv2.destroyAllWindows()
            break
        elif key == 32:
            img_name = "opencvframe{}.png".format(cpt)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            cpt += 1
            img_name = imutils.resizez(img_name,width=48,height=48)

@app.route('/res',methods = ['POST','GET'])
def res():
    global result
    if request.method == 'POST':
        result = request.form.to_dict()
        return render_template("results.html",result = result)

@app.route('/results')
def video_feed():
    global result
    params= result
    return Response(pyshine_process(params),mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == 'main':
    app.run(debug=True,host="172.20.10.3",port=9999,threaded=True)