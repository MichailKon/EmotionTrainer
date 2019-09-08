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
        self.Emotion = QtWidgets.QComboBox(Dialog)
        self.Emotion.setGeometry(QtCore.QRect(440, 40, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.Emotion.setFont(font)
        self.Emotion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Emotion.setEditable(False)
        self.Emotion.setObjectName("Emotion")
        self.Emotion.addItem("")
        self.Emotion.addItem("")
        self.Emotion.addItem("")
        self.Emotion.addItem("")
        self.Emotion.addItem("")
        self.Emotion.addItem("")
        self.Emotion.addItem("")
        self.ToMainWindow = QtWidgets.QPushButton(Dialog)
        self.ToMainWindow.setGeometry(QtCore.QRect(20, 430, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.ToMainWindow.setFont(font)
        self.ToMainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ToMainWindow.setObjectName("ToMainWindow")
        self.Image = QtWidgets.QLabel(Dialog)
        self.Image.setGeometry(QtCore.QRect(10, 40, 400, 350))
        self.Image.setText("")
        self.Image.setObjectName("Image")
        self.SetNextFace = QtWidgets.QPushButton(Dialog)
        self.SetNextFace.setGeometry(QtCore.QRect(462, 397, 131, 61))
        self.SetNextFace.setObjectName("SetNextFace")
        self.IsUserRight = QtWidgets.QLabel(Dialog)
        self.IsUserRight.setGeometry(QtCore.QRect(490, 350, 81, 31))
        self.IsUserRight.setText("")
        self.IsUserRight.setObjectName("IsUserRight")

        self.retranslateUi(Dialog)
        self.Emotion.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Emotion.setItemText(0, _translate("Dialog", "Neutral"))
        self.Emotion.setItemText(1, _translate("Dialog", "Happy"))
        self.Emotion.setItemText(2, _translate("Dialog", "Sad"))
        self.Emotion.setItemText(3, _translate("Dialog", "Angry"))
        self.Emotion.setItemText(4, _translate("Dialog", "Disgust"))
        self.Emotion.setItemText(5, _translate("Dialog", "Surprised", "Sup"))
        self.Emotion.setItemText(6, _translate("Dialog", "Fear"))
        self.ToMainWindow.setText(_translate("Dialog", "Back"))
        self.SetNextFace.setText(_translate("Dialog", "OK"))
