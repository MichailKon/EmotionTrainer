# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UITrainer.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 600)
        self.SetNextFace = QtWidgets.QPushButton(Dialog)
        self.SetNextFace.setGeometry(QtCore.QRect(780, 480, 201, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.SetNextFace.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.SetNextFace.setFont(font)
        self.SetNextFace.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SetNextFace.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SetNextFace.setStyleSheet("QPushButton\n"
"{\n"
"    background-color : rgb(0, 170, 0);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: gray;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color : rgb(0, 150, 0);\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: gray;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color : rgb(0, 100, 0);\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: gray;\n"
"    padding: 6px;\n"
"}")
        self.SetNextFace.setObjectName("SetNextFace")
        self.Image = QtWidgets.QLabel(Dialog)
        self.Image.setGeometry(QtCore.QRect(30, 60, 720, 480))
        self.Image.setFrameShape(QtWidgets.QFrame.Box)
        self.Image.setLineWidth(2)
        self.Image.setText("")
        self.Image.setObjectName("Image")
        self.Emotion = QtWidgets.QGroupBox(Dialog)
        self.Emotion.setGeometry(QtCore.QRect(760, 50, 231, 431))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.Emotion.setFont(font)
        self.Emotion.setStyleSheet("QGropBox#Emotions {\n"
"     background-color: red;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}")
        self.Emotion.setFlat(False)
        self.Emotion.setCheckable(False)
        self.Emotion.setObjectName("Emotion")
        self.Angry = QtWidgets.QRadioButton(self.Emotion)
        self.Angry.setGeometry(QtCore.QRect(10, 40, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Angry.setFont(font)
        self.Angry.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Angry.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Angry.setIconSize(QtCore.QSize(40, 40))
        self.Angry.setAutoExclusive(False)
        self.Angry.setObjectName("Angry")
        self.Disgust = QtWidgets.QRadioButton(self.Emotion)
        self.Disgust.setGeometry(QtCore.QRect(10, 90, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Disgust.setFont(font)
        self.Disgust.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Disgust.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Disgust.setIconSize(QtCore.QSize(40, 40))
        self.Disgust.setAutoExclusive(False)
        self.Disgust.setObjectName("Disgust")
        self.Fear = QtWidgets.QRadioButton(self.Emotion)
        self.Fear.setGeometry(QtCore.QRect(10, 140, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Fear.setFont(font)
        self.Fear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Fear.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Fear.setIconSize(QtCore.QSize(40, 40))
        self.Fear.setAutoExclusive(False)
        self.Fear.setObjectName("Fear")
        self.Happy = QtWidgets.QRadioButton(self.Emotion)
        self.Happy.setGeometry(QtCore.QRect(10, 190, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Happy.setFont(font)
        self.Happy.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Happy.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Happy.setIconSize(QtCore.QSize(40, 40))
        self.Happy.setAutoExclusive(False)
        self.Happy.setObjectName("Happy")
        self.Sad = QtWidgets.QRadioButton(self.Emotion)
        self.Sad.setGeometry(QtCore.QRect(10, 240, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Sad.setFont(font)
        self.Sad.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Sad.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Sad.setIconSize(QtCore.QSize(40, 40))
        self.Sad.setAutoExclusive(False)
        self.Sad.setObjectName("Sad")
        self.Surprised = QtWidgets.QRadioButton(self.Emotion)
        self.Surprised.setGeometry(QtCore.QRect(10, 290, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Surprised.setFont(font)
        self.Surprised.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Surprised.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Surprised.setIconSize(QtCore.QSize(40, 40))
        self.Surprised.setAutoExclusive(False)
        self.Surprised.setObjectName("Surprised")
        self.Neutral = QtWidgets.QRadioButton(self.Emotion)
        self.Neutral.setGeometry(QtCore.QRect(10, 340, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Neutral.setFont(font)
        self.Neutral.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Neutral.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Neutral.setIconSize(QtCore.QSize(40, 40))
        self.Neutral.setAutoExclusive(False)
        self.Neutral.setObjectName("Neutral")
        self.Scorn = QtWidgets.QRadioButton(self.Emotion)
        self.Scorn.setGeometry(QtCore.QRect(10, 390, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.Scorn.setFont(font)
        self.Scorn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Scorn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Scorn.setIconSize(QtCore.QSize(40, 40))
        self.Scorn.setAutoExclusive(False)
        self.Scorn.setObjectName("Scorn")
        self.ToMainWindow = QtWidgets.QPushButton(Dialog)
        self.ToMainWindow.setGeometry(QtCore.QRect(870, 550, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.ToMainWindow.setFont(font)
        self.ToMainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ToMainWindow.setStyleSheet("")
        self.ToMainWindow.setObjectName("ToMainWindow")
        self.Progress = QtWidgets.QProgressBar(Dialog)
        self.Progress.setGeometry(QtCore.QRect(30, 20, 761, 23))
        self.Progress.setProperty("value", 24)
        self.Progress.setObjectName("Progress")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.SetNextFace.setText(_translate("Dialog", "Check"))
        self.Emotion.setTitle(_translate("Dialog", "Выберите эмоцию"))
        self.Angry.setText(_translate("Dialog", "Angry"))
        self.Disgust.setText(_translate("Dialog", "Disgust"))
        self.Fear.setText(_translate("Dialog", "Fear"))
        self.Happy.setText(_translate("Dialog", "Happy"))
        self.Sad.setText(_translate("Dialog", "Sad"))
        self.Surprised.setText(_translate("Dialog", "Surprised"))
        self.Neutral.setText(_translate("Dialog", "Neutral"))
        self.Scorn.setText(_translate("Dialog", "Scorn"))
        self.ToMainWindow.setText(_translate("Dialog", "Back"))


