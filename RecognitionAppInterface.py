# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RecognitionAppInterface.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 600)
        self.Start_recognition = QtWidgets.QPushButton(Form)
        self.Start_recognition.setGeometry(QtCore.QRect(20, 20, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.Start_recognition.setFont(font)
        self.Start_recognition.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Start_recognition.setMouseTracking(False)
        self.Start_recognition.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Start_recognition.setToolTip("")
        self.Start_recognition.setStyleSheet("                    QPushButton:hover {\n"
"                    background-color: silver;\n"
"                    }\n"
"")
        self.Start_recognition.setAutoDefault(False)
        self.Start_recognition.setDefault(False)
        self.Start_recognition.setFlat(False)
        self.Start_recognition.setObjectName("Start_recognition")
        self.Image = QtWidgets.QLabel(Form)
        self.Image.setGeometry(QtCore.QRect(30, 90, 640, 480))
        self.Image.setText("")
        self.Image.setObjectName("Image")
        self.Result = QtWidgets.QLabel(Form)
        self.Result.setGeometry(QtCore.QRect(700, 180, 281, 211))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.Result.setFont(font)
        self.Result.setStyleSheet("")
        self.Result.setText("")
        self.Result.setObjectName("Result")
        self.user_answered = QtWidgets.QPushButton(Form)
        self.user_answered.setGeometry(QtCore.QRect(900, 110, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.user_answered.setFont(font)
        self.user_answered.setStyleSheet("")
        self.user_answered.setObjectName("user_answered")
        self.ToMainWindow = QtWidgets.QPushButton(Form)
        self.ToMainWindow.setGeometry(QtCore.QRect(800, 540, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.ToMainWindow.setFont(font)
        self.ToMainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ToMainWindow.setObjectName("ToMainWindow")
        self.UserInput = QtWidgets.QSpinBox(Form)
        self.UserInput.setGeometry(QtCore.QRect(900, 60, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.UserInput.setFont(font)
        self.UserInput.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.UserInput.setObjectName("UserInput")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Start_recognition.setText(_translate("Form", "Начать распознавание"))
        self.user_answered.setText(_translate("Form", "OK"))
        self.ToMainWindow.setText(_translate("Form", "Back"))
