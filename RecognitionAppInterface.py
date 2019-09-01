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
        self.Start_recognition.setGeometry(QtCore.QRect(60, 30, 171, 28))
        self.Start_recognition.setStyleSheet("QPushButton {\n"
"                    background-color: white;\n"
"                    text-align: center;\n"
"                    border: none;\n"
"                    font-size: 14px;\n"
"                    font-weight: bold\n"
"                    }\n"
"\n"
"                    QPushButton:hover {\n"
"                    background-color: silver;\n"
"                    }\n"
"\n"
"                    QPushButton:pressed {\n"
"                    background-color: red;\n"
"                    }\n"
"                ")
        self.Start_recognition.setObjectName("Start_recognition")
        self.Image = QtWidgets.QLabel(Form)
        self.Image.setGeometry(QtCore.QRect(30, 90, 640, 480))
        self.Image.setText("")
        self.Image.setObjectName("Image")
        self.user_input = QtWidgets.QLineEdit(Form)
        self.user_input.setGeometry(QtCore.QRect(700, 90, 281, 25))
        self.user_input.setObjectName("user_input")
        self.Result = QtWidgets.QLabel(Form)
        self.Result.setGeometry(QtCore.QRect(700, 180, 281, 211))
        self.Result.setStyleSheet("")
        self.Result.setObjectName("Result")
        self.user_answered = QtWidgets.QPushButton(Form)
        self.user_answered.setGeometry(QtCore.QRect(700, 130, 281, 25))
        self.user_answered.setStyleSheet("QPushButton {\n"
"                    background-color: white;\n"
"                    text-align: center;\n"
"                    border: none;\n"
"                    font-size: 14px;\n"
"                    font-weight: bold\n"
"                    }\n"
"\n"
"                    QPushButton:hover {\n"
"                    background-color: silver;\n"
"                    }\n"
"\n"
"                    QPushButton:pressed {\n"
"                    background-color: red;\n"
"                    }\n"
"                ")
        self.user_answered.setObjectName("user_answered")
        self.ToMainWindow = QtWidgets.QPushButton(Form)
        self.ToMainWindow.setGeometry(QtCore.QRect(760, 530, 93, 28))
        self.ToMainWindow.setObjectName("ToMainWindow")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Start_recognition.setText(_translate("Form", "Начать распознавание"))
        self.Result.setText(_translate("Form", "TextLabel"))
        self.user_answered.setText(_translate("Form", "OK"))
        self.ToMainWindow.setText(_translate("Form", "back"))
