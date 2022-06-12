from flask import Flask, Response
import cv2

app = Flask(__name__)
video = cv2.VideoCapture(0)


@app.route('/')
def index():
    return "Default Message"

def gen(video):
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
        
@app.route('/video_feed')
def video_feed():
    global video
    return Response(gen(video),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == 'main':
    app.run(host='172.20.10.3', port=2204, threaded=True)