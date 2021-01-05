# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'face_recogcLMAOp.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Face_Recognition(object):
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
        self.back = QPushButton(self.frame)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(40, 12, 61, 61))
        font = QFont()
        font.setFamily(u"Apple Symbols")
        font.setPointSize(23)
        self.back.setFont(font)
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
        self.camframe.raise_()
        self.back.raise_()
        Dataset_Capture.setCentralWidget(self.centralwidget)

        self.retranslateUi(Dataset_Capture)

        QMetaObject.connectSlotsByName(Dataset_Capture)
    # setupUi

    def retranslateUi(self, Dataset_Capture):
        Dataset_Capture.setWindowTitle(QCoreApplication.translate("Dataset_Capture", u"main", None))
        self.back.setText("")
        self.camframe.setText("")
    # retranslateUi

