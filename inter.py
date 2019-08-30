# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui',
# licensing of 'untitled.ui' applies.
#
# Created: Fri Aug 30 18:01:54 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 240, 93, 28))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    font-size: 14px;\n"
"    text-align: center;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: silver;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: red;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(150, 120, 104, 87))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Form", "Тык", None, -1))



