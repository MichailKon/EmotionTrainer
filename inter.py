# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui',
# licensing of 'untitled.ui' applies.
#
# Created: Sat Aug 31 11:19:55 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1061, 618)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(110, 60, 800, 480))
        self.widget.setStyleSheet("QWidget {\n"
"    alignment: center;\n"
"}")
        self.widget.setObjectName("widget")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))

