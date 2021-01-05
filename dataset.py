# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'datasetFkenWn.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dataset_Capture(object):
    def setupUi(self, Dataset_Capture):
        if not Dataset_Capture.objectName():
            Dataset_Capture.setObjectName(u"Dataset_Capture")
        Dataset_Capture.resize(1024, 576)
        self.centralwidget = QWidget(Dataset_Capture)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 1024, 576))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMouseTracking(True)
        self.frame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(0,0,0);\n"
"color: rgb(220,220,220);\n"
"}")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.face_rec = QLabel(self.frame)
        self.face_rec.setObjectName(u"face_rec")
        self.face_rec.setGeometry(QRect(230, 15, 561, 60))
        font = QFont()
        font.setFamily(u"Apple SD Gothic Neo")
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.face_rec.setFont(font)
        self.face_rec.setStyleSheet(u"color: rgb(254, 94, 114);\n"
"background-color: none;")
        self.face_rec.setAlignment(Qt.AlignCenter)
        self.successfully = QLabel(self.frame)
        self.successfully.setObjectName(u"successfully")
        self.successfully.setEnabled(True)
        self.successfully.setGeometry(QRect(260, 240, 501, 71))
        font1 = QFont()
        font1.setFamily(u"Phosphate")
        font1.setPointSize(36)
        self.successfully.setFont(font1)
        self.successfully.setStyleSheet(u"background-color: none;\n"
"color: rgb(254, 94, 114);\n"
"")
        self.successfully.setAlignment(Qt.AlignCenter)
        self.ok = QPushButton(self.frame)
        self.ok.setObjectName(u"ok")
        self.ok.setGeometry(QRect(670, 470, 91, 61))
        font2 = QFont()
        font2.setFamily(u"Apple Symbols")
        font2.setPointSize(30)
        self.ok.setFont(font2)
        self.ok.setMouseTracking(True)
        self.ok.setFocusPolicy(Qt.TabFocus)
        self.ok.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(246, 182, 163, 255), stop:1 rgba(254, 92, 113, 255));\n"
"color: rgb(0,0,0);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(250, 237, 223);\n"
"color: rgb(0,0,0);\n"
"border-radius:30px;\n"
"}\n"
"\n"
"\n"
"")
        self.ok.setAutoDefault(True)
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(260, 470, 501, 61))
        font3 = QFont()
        font3.setFamily(u"Apple Symbols")
        font3.setPointSize(36)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.lineEdit.setFont(font3)
        self.lineEdit.setTabletTracking(False)
        self.lineEdit.setFocusPolicy(Qt.StrongFocus)
        self.lineEdit.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.lineEdit.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"border-radius: 30px;\n"
"border: 2px solid rgb(250, 236, 222);\n"
"background-color: rgb(250, 236, 222);\n"
"color: rgb(0,0,0);\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"}\n"
"QLineEdit:focus {\n"
"border-radius: 30px;\n"
"border: 2px solid rgb(254, 94, 114);\n"
"background-color: rgb(0,0,0);\n"
"color: rgb(255, 255, 255);\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"}\n"
"")
        self.lineEdit.setInputMethodHints(Qt.ImhNone)
        self.lineEdit.setFrame(True)
        self.lineEdit.setEchoMode(QLineEdit.Normal)
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit.setClearButtonEnabled(False)
        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(260, 480, 500, 41))
        font4 = QFont()
        font4.setFamily(u"Apple SD Gothic Neo")
        font4.setPointSize(16)
        self.progressBar.setFont(font4)
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	\n"
"	background-color: rgb(252, 238, 224);\n"
"	color: rgb(0, 0, 0);\n"
"	border-style: none;\n"
"	border-radius: 20px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 20px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(246, 182, 163, 255), stop:1 rgba(254, 92, 113, 255));\n"
"}")
        self.progressBar.setValue(10)
        self.back = QPushButton(self.frame)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(40, 12, 61, 61))
        font5 = QFont()
        font5.setFamily(u"Apple Symbols")
        font5.setPointSize(23)
        self.back.setFont(font5)
        self.back.setMouseTracking(True)
        self.back.setFocusPolicy(Qt.TabFocus)
        self.back.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: none;\n"
"color: rgb(255,255,255);\n"
"border-radius:15px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(0,0,0);\n"
"color: rgb(0,0,0);\n"
"border-radius:15px;\n"
"}\n"
"\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u"bin/previous.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back.setIcon(icon)
        self.back.setIconSize(QSize(30, 30))
        self.back.setAutoDefault(True)
        self.camframe = QLabel(self.frame)
        self.camframe.setObjectName(u"camframe")
        self.camframe.setGeometry(QRect(0, 0, 1024, 576))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(60)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.camframe.sizePolicy().hasHeightForWidth())
        self.camframe.setSizePolicy(sizePolicy1)
        self.camframe.setContextMenuPolicy(Qt.NoContextMenu)
        self.camframe.setStyleSheet(u"")
        self.ok_2 = QPushButton(self.frame)
        self.ok_2.setObjectName(u"ok_2")
        self.ok_2.setGeometry(QRect(370, 130, 281, 281))
        self.ok_2.setFont(font2)
        self.ok_2.setMouseTracking(True)
        self.ok_2.setFocusPolicy(Qt.TabFocus)
        self.ok_2.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color:  rgb(0,0,0);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"bin/facerecognition.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ok_2.setIcon(icon1)
        self.ok_2.setIconSize(QSize(260, 260))
        self.ok_2.setAutoDefault(True)
        self.camframe.raise_()
        self.face_rec.raise_()
        self.lineEdit.raise_()
        self.progressBar.raise_()
        self.back.raise_()
        self.ok_2.raise_()
        self.successfully.raise_()
        self.ok.raise_()
        Dataset_Capture.setCentralWidget(self.centralwidget)

        self.retranslateUi(Dataset_Capture)

        QMetaObject.connectSlotsByName(Dataset_Capture)
    # setupUi

    def retranslateUi(self, Dataset_Capture):
        Dataset_Capture.setWindowTitle(QCoreApplication.translate("Dataset_Capture", u"main", None))
        self.face_rec.setText(QCoreApplication.translate("Dataset_Capture", u"<html><head/><body><p>FACE RECOGNITION</p></body></html>", None))
        self.successfully.setText(QCoreApplication.translate("Dataset_Capture", u"<html><head/><body><p>successfully !!!</p></body></html>", None))
        self.ok.setText(QCoreApplication.translate("Dataset_Capture", u"OK", None))
#if QT_CONFIG(tooltip)
        self.lineEdit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dataset_Capture", u"YOUR NAME", None))
        self.back.setText("")
        self.camframe.setText("")
        self.ok_2.setText("")
    # retranslateUi

