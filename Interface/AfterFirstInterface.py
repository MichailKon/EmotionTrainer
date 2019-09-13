# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AfterFirstInterface.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(681, 524)
        self.Statistics = QtWidgets.QTableWidget(Form)
        self.Statistics.setGeometry(QtCore.QRect(10, 10, 641, 411))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.Statistics.setFont(font)
        self.Statistics.setRowCount(10)
        self.Statistics.setColumnCount(4)
        self.Statistics.setObjectName("Statistics")
        item = QtWidgets.QTableWidgetItem()
        self.Statistics.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Statistics.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Statistics.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Statistics.setHorizontalHeaderItem(3, item)
        self.Statistics.horizontalHeader().setVisible(True)
        self.Statistics.horizontalHeader().setCascadingSectionResizes(False)
        self.Statistics.horizontalHeader().setDefaultSectionSize(150)
        self.Statistics.verticalHeader().setHighlightSections(True)
        self.ToMainWindow = QtWidgets.QPushButton(Form)
        self.ToMainWindow.setGeometry(QtCore.QRect(40, 450, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.ToMainWindow.setFont(font)
        self.ToMainWindow.setObjectName("ToMainWindow")
        self.ToAfterFirst = QtWidgets.QPushButton(Form)
        self.ToAfterFirst.setGeometry(QtCore.QRect(470, 450, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.ToAfterFirst.setFont(font)
        self.ToAfterFirst.setObjectName("ToAfterFirst")
        self.Image = QtWidgets.QLabel(Form)
        self.Image.setGeometry(QtCore.QRect(130, 40, 400, 350))
        self.Image.setText("")
        self.Image.setObjectName("Image")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.Statistics.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Image"))
        item = self.Statistics.horizontalHeaderItem(1)
        item.setText(_translate("Form", "True answer"))
        item = self.Statistics.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Your answer"))
        item = self.Statistics.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Time"))
        self.ToMainWindow.setText(_translate("Form", "Back"))
        self.ToAfterFirst.setText(_translate("Form", "Back"))
