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
        Dialog.resize(1000, 600)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(780, 470, 201, 61))
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
        self.pushButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setStyleSheet("QPushButton\n"
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
        self.pushButton.setObjectName("pushButton")
        self.Image = QtWidgets.QLabel(Dialog)
        self.Image.setGeometry(QtCore.QRect(30, 60, 720, 480))
        self.Image.setFrameShape(QtWidgets.QFrame.Box)
        self.Image.setLineWidth(2)
        self.Image.setText("")
        self.Image.setObjectName("Image")
        self.Emotions = QtWidgets.QGroupBox(Dialog)
        self.Emotions.setGeometry(QtCore.QRect(780, 50, 201, 401))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.Emotions.setFont(font)
        self.Emotions.setStyleSheet("QGropBox#Emotions {\n"
"     background-color: red;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}")
        self.Emotions.setFlat(False)
        self.Emotions.setCheckable(False)
        self.Emotions.setObjectName("Emotions")
        self.radioButton = QtWidgets.QRadioButton(self.Emotions)
        self.radioButton.setGeometry(QtCore.QRect(10, 40, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.radioButton.setFont(font)
        self.radioButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton.setIconSize(QtCore.QSize(40, 40))
        self.radioButton.setAutoExclusive(False)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.Emotions)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 90, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton_2.setIconSize(QtCore.QSize(40, 40))
        self.radioButton_2.setAutoExclusive(False)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.Emotions)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 140, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton_3.setIconSize(QtCore.QSize(40, 40))
        self.radioButton_3.setAutoExclusive(False)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.Emotions)
        self.radioButton_4.setGeometry(QtCore.QRect(10, 190, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton_4.setIconSize(QtCore.QSize(40, 40))
        self.radioButton_4.setAutoExclusive(False)
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.Emotions)
        self.radioButton_5.setGeometry(QtCore.QRect(10, 240, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton_5.setIconSize(QtCore.QSize(40, 40))
        self.radioButton_5.setAutoExclusive(False)
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.Emotions)
        self.radioButton_6.setGeometry(QtCore.QRect(10, 290, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.radioButton_6.setFont(font)
        self.radioButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton_6.setIconSize(QtCore.QSize(40, 40))
        self.radioButton_6.setAutoExclusive(False)
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(self.Emotions)
        self.radioButton_7.setGeometry(QtCore.QRect(10, 340, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.radioButton_7.setFont(font)
        self.radioButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton_7.setIconSize(QtCore.QSize(40, 40))
        self.radioButton_7.setAutoExclusive(False)
        self.radioButton_7.setObjectName("radioButton_7")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(860, 550, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Check"))
        self.Emotions.setTitle(_translate("Dialog", "Выберете эмоцию"))
        self.radioButton.setText(_translate("Dialog", "Angry"))
        self.radioButton_2.setText(_translate("Dialog", "Disgust"))
        self.radioButton_3.setText(_translate("Dialog", "Fear"))
        self.radioButton_4.setText(_translate("Dialog", "Happy"))
        self.radioButton_5.setText(_translate("Dialog", "Sad"))
        self.radioButton_6.setText(_translate("Dialog", "Surprise"))
        self.radioButton_7.setText(_translate("Dialog", "Neutral"))
        self.pushButton_2.setText(_translate("Dialog", "Back"))
