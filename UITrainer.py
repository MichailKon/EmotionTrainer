# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UITrainer.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(440, 40, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 430, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.Image = QtWidgets.QLabel(Dialog)
        self.Image.setGeometry(QtCore.QRect(10, 40, 411, 351))
        self.Image.setText("")
        self.Image.setObjectName("Image")

        self.retranslateUi(Dialog)
        self.comboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.comboBox.setItemText(0, _translate("Dialog", "Neutral"))
        self.comboBox.setItemText(1, _translate("Dialog", "Happy"))
        self.comboBox.setItemText(2, _translate("Dialog", "Sad"))
        self.comboBox.setItemText(3, _translate("Dialog", "Angry"))
        self.comboBox.setItemText(4, _translate("Dialog", "Disgust"))
        self.comboBox.setItemText(5, _translate("Dialog", "Surprised", "Sup"))
        self.comboBox.setItemText(6, _translate("Dialog", "Fear"))
        self.pushButton.setText(_translate("Dialog", "Back"))
