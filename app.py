from flask import Flask, render_template,request,Response
import cv2,imutils,time
import pyshine as ps
#import cv2,imutils,time
#import pyshine as ps
app = Flask(__name__)
@app.route('/')
def anyname():
   return render_template('index.html')

if __name__ == '__main__':
    app.run(host="172.20.10.3",debug=False,port=9999)