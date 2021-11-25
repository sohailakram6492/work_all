import numpy as np
import os, cv2 ,json
import easyocr
from datetime import datetime
def fun():

    reader = easyocr.Reader(['en'])
    face_detect = False
    if os.path.exists('static/face.jpg'):
        os.remove('static/face.jpg')
    if os.path.exists(rf'static\text\data.json'):
        os.remove(rf'static\text\data.json')

    face_cascade = cv2.CascadeClassifier('model\haar_cascade.xml')

    def face_detection(img):
        if os.path.exists('./static/face.jpg'):
            return img
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        box, detections = face_cascade.detectMultiScale2(gray, minNeighbors=8)
        for x, y, w, h in box:
            if len(detections) > 0 and detections[0] > 60:
                # cv2.rectangle(img,(x-30,y-30),(x+w+30,y+h+30),(0,255,0),1)
                face = img[y-30:y+h+30, x-30:x+w+30]
                cv2.imwrite('./static/face.jpg', face)
                global face_detect
                face_detect = True
                return face
            else:
                print(detections)
                return img
    cap = cv2.VideoCapture('videos\output2.avi')
    while True:
        ret, frame = cap.read()
        if ret == False:
            break
        if not face_detect:
            face_detection(frame)
        else:
            print('face has been detected stop detection')
            break
    dictnary = {
        "name": '-',
        "father name": '-',
        "Id_Number": '-',
        "Gender":"-",
        "Dates": [] }
    cap.release()
    cap1 = cv2.VideoCapture('videos\output2.avi')

    is_filed = False
    count =0
    while not is_filed:
        ret, frame = cap1.read()
        if count%10==0:
            result = reader.readtext(frame)
        for index in range(len(result)):
            if result[index][2] >.5:
                if '-' not in dictnary.values() and len(dictnary['Dates']) == 3:
                    is_filed = True
                    break
                elif result[index][1].lower() == 'name':
                    dictnary['name'] = result[index+1][1]
                elif result[index][1].lower() == 'father name':
                    dictnary['father name'] = result[index+1][1]
                elif result[index][1].count('-') == 2:
                    dictnary["Id_Number"] = result[index][1]
                elif result[index][1].count('.') == 2 and result[index][2]>.9 and (result[index][1] not in dictnary['Dates']):
                    dictnary['Dates'].append(result[index][1])
                elif result[index][1].lower() == 'm':
                    dictnary['Gender'] = 'Male'
                elif result[index][1].lower() == 'f':
                    dictnary['Gender'] = 'Female'
        dictnary['Dates'].sort(key=lambda x: datetime.strptime(x, '%d.%m.%Y'))
        print(result)
        print(dictnary)
    cap1.release()
    file = json.dumps(dictnary, indent=4)
    with open('./static/text/data.json', 'w') as f:
        f.write(file)
