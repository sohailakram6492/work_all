
# Easy-OCR text recongnition and haar_Cascade_Classifier for face detection

These are some libraries that must be imported first for the execution of this project.
1. numpy as np
2. os
3. cv2 
4. json
5. easyocr
6. from datetime import datetime
7. from flask import Flask, render_template, Response
8. detection

A brief description of what this project does and who it's for

These are some libraries that must be imported first for the execution of this project.
1. numpy as np
2. os
3. cv2 
4. json
5. easyocr
6. from datetime import datetime
7. from flask import Flask, render_template, Response
8. detection

This project recognizes the text given to it, through any way like from alive webcam, picture, or video. This project not only recognizes the text area but also gives its location and accuracy, means how much accuratly it recognizes the text, In this project I have used easyocr python pakage that is revolutionary for the digital world nowadays. 

Optical Character Recognition is actually a complete process under which the images/documents which are present in a digital world are processed and from the text are being processed out as normal editable text.
Actually, this project is specifically made for the Pakistani National Identity Card, this project not only recognize the text like name, father name, date of birth, date of issue, and date of expire for the CINIC not only text it also detects the image from it.
After all detection and recognition, this program will store all the data or images that are available in your local storage.

In the first app.py file, I have created a basic flask app for displaying the result on a web browser and use some basic CV2 functions for converting video into frames so that it can be processed further.

In the second detection.py file, I have placed all my code in the fun() function, so that it can be executed easily and return output to  app.py so that it can easily be rendered into web_browser. There is a function face_detection that detect face from our CNIC and after face detection, our text recognition starts which extract all the data and store that with the help of a dictionary in which I have predefined all the key and store their corresponding values with the help of code.

In the remaining HTML pages, I have created three pages for the Flask app on a Home page I have created two buttons, one to start the video from our webcam and the other to directly go to the result without recoding the video and preprocess previously recoded video and display result. If you will click on the video recode button, it will redirect you to start the video page in which video recording will be started and there is a button that will stop your recording when you press it.

IMPORTANT POINT:
Try to recode a short and clear video as much as you can otherwise, it will take a lot of time because it has to process all the frames.


## Authors

- [Muhammad Sohail Akram](https://github.com/sohailakram6492)



## Installation

Basic Installation.
Install Python 3.7 or above any version
Download and install VS Code 

Open cmd 
Run these commends in it.

```bash
  git https://github.com/sohailakram6492/cnic_text_detection.git
  cd clone cnic_text_detection
  code . # this will open vs code and select your folder.
  Run this commend in terminal.
  pip install requirments.txt

```
    
## Appendix

OUTPUTS:

{([[439, 322], [543, 322], [543, 354], [439, 354]], 'Q1ault', 0.01823662566777131), ([[311, 359], [399, 359], [399, 375], [311, 375]], 'Date of Expiry', 0.9464883358566832), ([[169, 367], [251, 367], [251, 383], [169, 383]], 'Date of Issue', 0.6978377929416322), ([[174, 378], [258, 378], [258, 404], [174, 404]], '15.06.2021', 0.9024466714113487), ([[316, 370], [398, 370], [398, 396], [316, 396]], '15.06.2031', 0.988977049044154), ([[433, 385], [477, 385], [477, 399], [433, 399]], 'Heldee', 0.10997907415707031), ([[483, 381], [543, 381], [543, 397], [483, 397]], 'Signature', 0.6815505236369251), ([[55, 409], [125, 409], [125, 436], [55, 436]], '42 ', 0.033436759776801675)]
{'name': 'Saleem Ullah', 'father name': 'Ghulam Ullah Usmani', 'Id_Number': '35201-5399394-5', 'Gender': 'Male', 'Dates': ['15.01.1996', '15.06.2021', '15.06.2031']}


EasyOCR
After installing the PyTorch library successfully it’s quite easy to install the EasyOCR library, one just has to run the following command:

1. Reading images
Taking an online image: Here we will take an image from a URL (online)
IMAGE_PATH = 'https://blog.aspose.com/wp-content/uploads/sites/2/2020/05/Perform-OCR-using-C.jpg'
In the above code snippet, one can notice that the IMAGE_PATH holds the URL of the image.

Taking image as input locally: Here we will take an image from the local system.
IMAGE_PATH = 'Perform-OCR.jpg'
In the above code snippet, one can notice that I have taken the image locally i.e. from the local system.

2. Extracting text from the image
English text detection
reader = easyocr.Reader(['en'])
result = reader.readtext(IMAGE_PATH,paragraph="False")
result
## Demo

Text will be displayed like this:

Name	Saleem Ullah

father name	Ghulam Ullah Usmani

ID-Number	35222-53000394-2

Gender	Male

Date-Of-Birth	15.01.1996

Date-Of-Issue	15.06.2021

Date-Of-Expire	15.06.2031

## Documentation

[Text detection from images using EasyOCR: Hands-on guide
](https://www.analyticsvidhya.com/blog/2021/06/text-detection-from-images-using-easyocr-hands-on-guide/)


