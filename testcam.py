from flask import Flask, render_template,request,Response
import cv2,imutils,time
import pyshine as ps

app = Flask(__name__)
@app.route('/')
def anyname():
   return render_template('index.html')
@app.route('/cam')
def camtest():
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
            img_name = "opencv_frame_{}.png".format(cpt)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            cpt += 1
camtest()
if __name__ == '__main__':
    app.run(host="172.20.10.3",debug=False,port=9999)