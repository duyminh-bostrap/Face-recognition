# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formrbTVkG.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_main_interface(object):
    def setupUi(self, main_interface):
        if not main_interface.objectName():
            main_interface.setObjectName(u"main_interface")
        main_interface.resize(600, 900)
        self.centralwidget = QWidget(main_interface)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 600, 900))
        self.frame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(56,58,89);\n"
"color: rgb(220,220,220);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 0, 601, 321))
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.frame_3)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(0, 0, 600, 301))
        font = QFont()
        font.setFamily(u"Apple SD Gothic Neo")
        font.setPointSize(28)
        font.setStyleStrategy(QFont.NoAntialias)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"QLabel{\n"
"border-radius: 40px;\n"
"color: rgb(254, 121, 199);\n"
"}")
        self.label_title.setPixmap(QPixmap(u"bin/screen.png"))
        self.label_title.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_title_3 = QLabel(self.frame_3)
        self.label_title_3.setObjectName(u"label_title_3")
        self.label_title_3.setGeometry(QRect(70, 65, 251, 31))
        font1 = QFont()
        font1.setFamily(u"Apple SD Gothic Neo")
        font1.setPointSize(27)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_title_3.setFont(font1)
        self.label_title_3.setStyleSheet(u"QLabel{\n"
"border: 40px;\n"
"background-color: none;\n"
"color: rgb(0,0,0);\n"
"}")
        self.label_title_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 260, 601, 681))
        font2 = QFont()
        font2.setFamily(u"Apple SD Gothic Neo")
        self.frame_2.setFont(font2)
        self.frame_2.setStyleSheet(u"QFrame{\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(246, 182, 163, 255), stop:0.663366 rgba(214, 66, 86, 255));\n"
"color: rgb(220,220,220);\n"
"border-radius:40px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.pushButton_recog = QPushButton(self.frame_2)
        self.pushButton_recog.setObjectName(u"pushButton_recog")
        self.pushButton_recog.setGeometry(QRect(70, 80, 211, 291))
        font3 = QFont()
        font3.setFamily(u"Apple Symbols")
        font3.setPointSize(24)
        self.pushButton_recog.setFont(font3)
        self.pushButton_recog.setAutoFillBackground(False)
        self.pushButton_recog.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: rgb(254,240,226);\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(246, 182, 163, 255), stop:1 rgba(254, 92, 113, 255));\n"
"border-radius:25px;\n"
"padding-bottom: 50px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(255,255,255);\n"
"color: rgb(130,144,217);\n"
"border-radius:25px;\n"
"}\n"
"\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u"bin/face-recog.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_recog.setIcon(icon)
        self.pushButton_recog.setIconSize(QSize(80, 80))
        self.pushButton_recog.setAutoDefault(True)
        self.face_recognition = QLabel(self.frame_2)
        self.face_recognition.setObjectName(u"face_recognition")
        self.face_recognition.setGeometry(QRect(110, 270, 131, 71))
        font4 = QFont()
        font4.setFamily(u"Apple SD Gothic Neo")
        font4.setPointSize(22)
        font4.setBold(True)
        font4.setWeight(75)
        self.face_recognition.setFont(font4)
        self.face_recognition.setStyleSheet(u"QLabel{\n"
"border: 40px;\n"
"background-color: none;\n"
"color: rgb(0,0,0);\n"
"}")
        self.face_recognition.setAlignment(Qt.AlignCenter)
        self.pushButton_playrecord = QPushButton(self.frame_2)
        self.pushButton_playrecord.setObjectName(u"pushButton_playrecord")
        self.pushButton_playrecord.setGeometry(QRect(310, 290, 211, 171))
        self.pushButton_playrecord.setFont(font3)
        self.pushButton_playrecord.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: rgb(254,240,226);\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(246, 182, 163, 255), stop:1 rgba(254, 92, 113, 255));\n"
"border-radius:25px;\n"
"padding-bottom: 30px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(255,255,255);\n"
"color: rgb(130,144,217);\n"
"border-radius:25px;\n"
"}\n"
"\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"bin/pl_record.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_playrecord.setIcon(icon1)
        self.pushButton_playrecord.setIconSize(QSize(75, 75))
        self.pushButton_exit = QPushButton(self.frame_2)
        self.pushButton_exit.setObjectName(u"pushButton_exit")
        self.pushButton_exit.setGeometry(QRect(310, 490, 211, 61))
        self.pushButton_exit.setFont(font4)
        self.pushButton_exit.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: rgb(254,240,226);\n"
"color: rgb(0, 0, 0);\n"
"border-radius:25px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(255,255,255);\n"
"border-radius:25px;\n"
"}\n"
"\n"
"\n"
"")
        self.play_record = QLabel(self.frame_2)
        self.play_record.setObjectName(u"play_record")
        self.play_record.setGeometry(QRect(340, 415, 151, 31))
        self.play_record.setFont(font4)
        self.play_record.setStyleSheet(u"QLabel{\n"
"border: 40px;\n"
"background-color: none;\n"
"color: rgb(0,0,0);\n"
"}")
        self.play_record.setAlignment(Qt.AlignCenter)
        self.create_faceid = QLabel(self.frame_2)
        self.create_faceid.setObjectName(u"create_faceid")
        self.create_faceid.setGeometry(QRect(330, 210, 171, 31))
        self.create_faceid.setFont(font4)
        self.create_faceid.setStyleSheet(u"QLabel{\n"
"border: 40px;\n"
"background-color: none;\n"
"color: rgb(0,0,0);\n"
"}")
        self.create_faceid.setAlignment(Qt.AlignCenter)
        self.pushButton_record = QPushButton(self.frame_2)
        self.pushButton_record.setObjectName(u"pushButton_record")
        self.pushButton_record.setGeometry(QRect(70, 400, 211, 151))
        self.pushButton_record.setFont(font3)
        self.pushButton_record.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: rgb(254,240,226);\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(246, 182, 163, 255), stop:1 rgba(254, 92, 113, 255));\n"
"border-radius:25px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(255,255,255);\n"
"color: rgb(130,144,217);\n"
"border-radius:25px;\n"
"}\n"
"\n"
"\n"
"")
        self.record = QLabel(self.frame_2)
        self.record.setObjectName(u"record")
        self.record.setGeometry(QRect(140, 500, 71, 31))
        self.record.setFont(font4)
        self.record.setStyleSheet(u"QLabel{\n"
"border: 40px;\n"
"background-color: none;\n"
"color: rgb(0,0,0);\n"
"}")
        self.record.setAlignment(Qt.AlignCenter)
        self.toolButton = QToolButton(self.frame_2)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(140, 440, 71, 41))
        self.toolButton.setStyleSheet(u"QToolButton{\n"
"background-color: rgb(0,0,0);\n"
"color: rgb(220,220,220);\n"
"border-radius:20px;\n"
"}")
        self.pushButton_faceid = QPushButton(self.frame_2)
        self.pushButton_faceid.setObjectName(u"pushButton_faceid")
        self.pushButton_faceid.setGeometry(QRect(310, 80, 211, 181))
        self.pushButton_faceid.setFont(font3)
        self.pushButton_faceid.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: rgb(254,240,226);\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(246, 182, 163, 255), stop:1 rgba(254, 92, 113, 255));\n"
"border-radius:25px;\n"
"padding-bottom: 30px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(255,255,255);\n"
"color: rgb(130,144,217);\n"
"border-radius:25px;\n"
"}\n"
"\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"bin/cr_faceid.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_faceid.setIcon(icon2)
        self.pushButton_faceid.setIconSize(QSize(80, 80))
        self.toolButton_2 = QToolButton(self.frame_2)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setGeometry(QRect(144, 444, 33, 33))
        self.toolButton_2.setStyleSheet(u"QToolButton{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(220,220,220);\n"
"border-radius:16px;\n"
"}")
        self.pushButton_faceid.raise_()
        self.pushButton_recog.raise_()
        self.face_recognition.raise_()
        self.pushButton_playrecord.raise_()
        self.pushButton_exit.raise_()
        self.play_record.raise_()
        self.create_faceid.raise_()
        self.pushButton_record.raise_()
        self.record.raise_()
        self.toolButton.raise_()
        self.toolButton_2.raise_()
        main_interface.setCentralWidget(self.centralwidget)

        self.retranslateUi(main_interface)

        QMetaObject.connectSlotsByName(main_interface)
    # setupUi


    def retranslateUi(self, main_interface):
        main_interface.setWindowTitle(QCoreApplication.translate("main_interface", u"Face Recognition", None))
        self.label_title.setText("")
        self.label_title_3.setText(QCoreApplication.translate("main_interface", u"<html><head/><body><p>FACE RECOGNITION</p></body></html>", None))
        self.pushButton_recog.setText("")
        self.face_recognition.setText(QCoreApplication.translate("main_interface", u"<html><head/><body><p align=\"center\">Face</p><p align=\"center\">Recognition</p></body></html>", None))
        self.pushButton_playrecord.setText("")
        self.pushButton_exit.setText(QCoreApplication.translate("main_interface", u"Exit", None))
        self.play_record.setText(QCoreApplication.translate("main_interface", u"Play Record", None))
        self.create_faceid.setText(QCoreApplication.translate("main_interface", u"Create FaceID", None))
        self.pushButton_record.setText("")
        self.record.setText(QCoreApplication.translate("main_interface", u"Record", None))
        self.toolButton.setText("")
        self.pushButton_faceid.setText("")
        self.toolButton_2.setText("")
    # retranslateUi

