import sys
import cv2
import os
import numpy as np
from PIL import Image
import face_recognition
import pickle
import platform
from datetime import datetime
from PySide2 import QtCore
from PySide2.QtCore import QRect, QTimer
from PySide2.QtGui import QColor, QImage, QPixmap
from PySide2.QtWidgets import *

# ==> SPLASH SCREEN
from splash_screen import Ui_SplashScreen
# ==> MAIN WINDOW
from main_interface import Ui_main_interface
# ==> DATASETS WINDOW
from dataset import Ui_Dataset_Capture
# ==> FaceRecogniton WINDOW
from face_recog import Ui_Face_Recognition
# ==> Record WINDOW
from open_record import Ui_Record

# ==> GLOBALS
counter = 0
record_value = 0


class MainWindow(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_main_interface()
        self.ui.setupUi(self)

        # REMOVE TITLE BAR
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Click button
        self.ui.pushButton_recog.clicked.connect(self.clickFaceRecord)
        self.ui.pushButton_faceid.clicked.connect(self.clickCFID)
        self.ui.pushButton_playrecord.clicked.connect(self.clickPlayRecord)
        self.ui.toolButton.clicked.connect(self.clickTurnRecord)
        self.ui.toolButton_2.clicked.connect(self.clickTurnRecord)
        self.ui.pushButton_exit.clicked.connect(self.clickExit)

        # show window
        self.show()

    def clickFaceRecord(self):
        """if self.record_value == 1:
            os.system("python3 recognition_record.py")
        elif self.record_value == 0:
            os.system("python3 face_recognition.py")"""
        self.main = FaceRecogniton()
        self.main.show()
        self.close()


    def clickCFID(self):
        self.main = Dataset()
        self.main.show()
        self.close()

    def clickTurnRecord(self):
        global record_value
        if record_value == 0:
            record_value = 1
            self.ui.toolButton_2.setGeometry(QRect(174, 444, 33, 33))
            self.ui.toolButton.setStyleSheet(u"QToolButton{\n"
                                             "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(246, 182, 163, 255), stop:1 rgba(254, 92, 113, 255));\n"
                                             "color: rgb(220,220,220);\n"
                                             "border-radius:20px;\n"
                                             "}")
        elif record_value == 1:
            record_value = 0
            self.ui.toolButton_2.setGeometry(QRect(144, 444, 33, 33))
            self.ui.toolButton.setStyleSheet(u"QToolButton{\n"
                                             "background-color: rgb(0,0,0);\n"
                                             "color: rgb(220,220,220);\n"
                                             "border-radius:20px;\n"
                                             "}")
        print(record_value)

    def clickPlayRecord(self):
        self.main = Record()
        self.main.show()
        self.close()

    def clickExit(self):
        self.close()


class Dataset(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Dataset_Capture()
        self.ui.setupUi(self)

        # REMOVE TITLE BAR
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Click Create dataset
        # create a timer
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.Create_dataset)
        # set control_bt callback clicked  function
        self.ui.ok.clicked.connect(self.controlTimer)
        self.ui.back.clicked.connect(self.clickBack)

        # show window
        self.show()
        self.ui.progressBar.hide()
        self.ui.successfully.hide()

        # MAIN WINDOW LABEL
        # QtCore.QTimer.singleShot(1500, lambda: self.ui.label.setText("<strong>THANKS</strong> FOR WATCHING"))
        # QtCore.QTimer.singleShot(1500, lambda: self.setStyleSheet("background-color: #222; color: #FFF"))

    def clickBack(self):
        self.FaceRecogniton = MainWindow()
        self.FaceRecogniton.show()
        self.close()

    def controlTimer(self):
        if not self.timer.isActive():
            self.timer.start(20)
        else:
            self.timer.stop()
            self.cap.release()

        self.cap = cv2.VideoCapture(0)
        self.ui.progressBar.show()
        self.ui.lineEdit.hide()
        self.ui.ok.hide()
        self.ui.ok_2.hide()
        self.ui.face_rec.hide()
        # self.ui.label_title_2.show
        self.face_id = 1
        # Start capturing video
        self.face_detector = cv2.CascadeClassifier('./cascades/data/haarcascade_frontalface_default.xml')
        # Initialize sample face image
        self.count = 10

        # create file object
        self.name = self.ui.lineEdit.text()
        """path = "./datasets/" + self.name
        try:
            os.mkdir(path)
        except OSError:
            print("Creation of the directory %s failed" % path)
        else:
            print("Successfully created the directory %s " % path)"""

    def Create_dataset(self):
        _, image_frame = self.cap.read()
        gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_detector.detectMultiScale(gray, 1.3, 5)

        image_frame = cv2.cvtColor(image_frame, cv2.COLOR_BGR2RGB)
        image_frame = cv2.resize(image_frame, (1024, 576))
        # get image infos
        height, width, channel = image_frame.shape
        step = channel * width

        # Loops for each faces
        for (x, y, w, h) in faces:
            # Crop the image frame into rectangle
            if self.count <= 100:
                cv2.rectangle(image_frame, (int(x * 0.8), int(y * 0.8)), (int((x + w) * 0.8), int((y + h) * 0.8)),
                              (254, 94, 114), 5)
            # Increment sample face image
            self.count += 2
            self.ui.progressBar.setValue(self.count)
            # Save the captured image into the datasets folder
            cv2.imwrite("datasets/" + self.name + ".jpg", gray[y:y + h, x:x + w])

            # Display the video frame, with bounded rectangle on the person's face
            # cv2.imshow('Create Dataset', image_frame)
        # create QImage from image
        qImg = QImage(image_frame.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        self.ui.camframe.setPixmap(QPixmap.fromImage(qImg))
        if self.count > 100:
            self.ui.successfully.show()
            self.ui.face_rec.show()
            self.timer.stop()
            self.cap.release()


class FaceRecogniton(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Face_Recognition()
        self.ui.setupUi(self)

        # REMOVE TITLE BAR
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Click Create dataset
        # create a timer
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.Play_record)
        # set control_bt callback clicked  function
        self.controlTimer()
        self.ui.back.clicked.connect(self.clickBack)

        # show window
        self.show()

    def clickBack(self):
        self.FaceRecogniton = MainWindow()
        self.FaceRecogniton.show()
        self.close()
        self.timer.stop()
        self.cap.release()

    def controlTimer(self):
        if not self.timer.isActive():
            self.timer.start(20)
        else:
            self.timer.stop()
            self.cap.release()

        self.cap = cv2.VideoCapture(0)
        path = 'datasets'
        images = []
        self.classNames = []
        myList = os.listdir(path)
        print(myList)
        for cl in myList:
            curImg = cv2.imread(f'{path}/{cl}')
            # if cl.endswith(".jpg"):
            images.append(curImg)
            self.classNames.append(os.path.splitext(cl)[0])
        print(self.classNames)
        print('Encoding Complete')
        self.encodeListKnown = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            self.encodeListKnown.append(encode)
        if record_value == 1:
            self.out = cv2.VideoWriter('./saved-media/record.avi', cv2.VideoWriter_fourcc('F','F','V','1'), self.cap.get(cv2.CAP_PROP_FPS), (1024, 576))
        #self.out = cv2.VideoWriter('./saved-media/record.mp4', video_type_cv2, 24.0, (1024, 576))

    def Play_record(self):
        success, image_frame = self.cap.read()
        # img = captureScreen()
        # convert image to RGB format
        image_frame = cv2.resize(image_frame, (0, 0), None, 0.8, 0.8)
        image_frame = cv2.cvtColor(image_frame, cv2.COLOR_BGR2RGB)
        """image_frame = cv2.cvtColor(image_frame, cv2.COLOR_BGR2RGB)
        image_frame = cv2.resize(image_frame, (1024, 576))"""
        facesCurFrame = face_recognition.face_locations(image_frame)
        encodesCurFrame = face_recognition.face_encodings(image_frame, facesCurFrame)
        # get image infos
        height, width, channel = image_frame.shape
        step = channel * width

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(self.encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(self.encodeListKnown, encodeFace)
            # print(faceDis)
            matchIndex = np.argmin(faceDis)

            name = "unknown".upper()
            # print(name)
            y1, x2, y2, x1 = faceLoc
            # print(str(y1) +" " +str(x2) + " " +str(y2)+" "+str(x1))
            y1, x2, y2, x1 = int(y1*0.9), int(x2*1.05), int(y2), int(x1*0.95)
            cv2.rectangle(image_frame, (x1, y1), (x2, y2), (254, 94, 114), 2)
            cv2.rectangle(image_frame, (x1, y1 + 38), (x2, y1), (254, 94, 114), cv2.FILLED)

            if matches[matchIndex]:
                name = self.classNames[matchIndex].upper()
                # self.markAttendance(name)
            cv2.putText(image_frame, name, (x1 + 8, y1 + 27), cv2.FONT_HERSHEY_COMPLEX, 1, (254, 240, 226), 2)
        # cv2.imshow('Webcam', image_frame)
        # cv2.title("Face Recogniton")
        if success and record_value == 1:
            self.out.write(image_frame)
        qImg = QImage(image_frame.data, width, height, step, QImage.Format_RGB888)
        self.ui.camframe.setPixmap(QPixmap.fromImage(qImg))


class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        # UI ==> INTERFACE CODES
        ########################################################################

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        # QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText("<strong>WELCOME</strong> TO MY APPLICATION")

        # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> ..."))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> INTERFACE"))

        # SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        # ==> END ##

    # ==> APP FUNCTIONS
    ########################################################################
    def progress(self):
        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1


class Record(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Record()
        self.ui.setupUi(self)

        # REMOVE TITLE BAR
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Click Create dataset
        # create a timer
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.Play_record)
        # set control_bt callback clicked  function
        self.controlTimer()
        self.ui.back.clicked.connect(self.clickBack)

        # show window
        self.show()

    def clickBack(self):
        self.FaceRecogniton = MainWindow()
        self.FaceRecogniton.show()
        self.close()
        self.timer.stop()
        self.cap.release()

    def controlTimer(self):
        if not self.timer.isActive():
            self.timer.start(200)
        else:
            self.timer.stop()
            self.cap.release()

        self.cap = cv2.VideoCapture('./saved-media/record.avi')

    def Play_record(self):
        ret, frames = self.cap.read()
        #frames = cv2.resize(frame, (1024, 576))h
        height, width, channel = frames.shape
        step = channel * width
        qImg = QImage(frames.data, width, height, step, QImage.Format_RGB888)
        self.ui.camframe.setPixmap(QPixmap.fromImage(qImg))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    # window = MainWindow()
    sys.exit(app.exec_())
