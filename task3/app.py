from flask import Flask, render_template, Response
import cv2
import detection, json, os

app = Flask(__name__)

camera = cv2.VideoCapture()

def use_camera():
    global camera
    camera = cv2.VideoCapture(0)

def release_camera():
    global camera
    if camera.isOpened():
        camera.release()

def gen_frames():
    fourcc =cv2.VideoWriter_fourcc(*'XVID')
    out =cv2.VideoWriter('./videos/output1.avi',fourcc,20.0,(640,480))
    while True:
        success, frame = camera.read() # read the camera frame
        out.write(frame)
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
@app.route("/")
def index():
    release_camera()
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    use_camera()
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/start_video1')
def start_video():
    return render_template('start_video.html')

@app.route('/stop')
def stop_video():
    release_camera()
    if os.path.exists('./static/text/data.json'):
        os.remove('./static/text/data.json')
    detection.fun()
    if os.path.exists('./static/text/data.json'):
        f = json.load(open('./static/text/data.json'))
    else:
        f = ''
    return render_template('stop.html', data = f)

if __name__ == '__main__':
    app.run(debug= True, port = 8000)