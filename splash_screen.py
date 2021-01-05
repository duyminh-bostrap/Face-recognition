# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screenauOLkU.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(620, 420)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setEnabled(True)
        self.dropShadowFrame.setMinimumSize(QSize(600, 400))
        self.dropShadowFrame.setMaximumSize(QSize(600, 400))
        self.dropShadowFrame.setStyleSheet(u"QFrame {	\n"
"	background-color: rgb(0,0,0);	\n"
"	color: rgb(220, 220, 220);\n"
"	border-radius: 40px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label_description = QLabel(self.dropShadowFrame)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(0, 130, 600, 31))
        font = QFont()
        font.setFamily(u"Apple SD Gothic Neo")
        font.setPointSize(15)
        self.label_description.setFont(font)
        self.label_description.setStyleSheet(u"color: rgb(254, 240, 226);")
        self.label_description.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(50, 270, 500, 30))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	\n"
"	background-color: rgb(252, 238, 224);\n"
"	color: rgb(0, 0, 0);\n"
"	border-style: none;\n"
"	border-radius: 15px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 15px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(246, 182, 163, 255), stop:1 rgba(254, 92, 113, 255));\n"
"}")
        self.progressBar.setValue(24)
        self.label_loading = QLabel(self.dropShadowFrame)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setGeometry(QRect(0, 310, 600, 21))
        font1 = QFont()
        font1.setFamily(u"Apple SD Gothic Neo")
        font1.setPointSize(13)
        self.label_loading.setFont(font1)
        self.label_loading.setStyleSheet(u"color: rgb(254, 240, 226);")
        self.label_loading.setAlignment(Qt.AlignCenter)
        self.label_credits = QLabel(self.dropShadowFrame)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setGeometry(QRect(110, 350, 441, 21))
        font2 = QFont()
        font2.setFamily(u"Apple SD Gothic Neo")
        font2.setPointSize(11)
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color: rgb(254, 240, 226);")
        self.label_credits.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_title_2 = QLabel(self.dropShadowFrame)
        self.label_title_2.setObjectName(u"label_title_2")
        self.label_title_2.setGeometry(QRect(10, 70, 600, 60))
        font3 = QFont()
        font3.setFamily(u"Apple SD Gothic Neo")
        font3.setPointSize(40)
        self.label_title_2.setFont(font3)
        self.label_title_2.setStyleSheet(u"color: rgb(254, 94, 114);")
        self.label_title_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.dropShadowFrame)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"Face Recognition", None))
        self.label_description.setText(QCoreApplication.translate("SplashScreen", u"<strong>APP</strong> DESCRIPTION", None))
        self.label_loading.setText(QCoreApplication.translate("SplashScreen", u"loading...", None))
        self.label_credits.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p><span style=\" font-weight:600;\">Created</span>: Duy Minh</p></body></html>", None))
        self.label_title_2.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p>FACE RECOGNITION</p></body></html>", None))
    # retranslateUi

