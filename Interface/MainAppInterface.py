# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainInterface.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.ToSecondTrainer = QtWidgets.QPushButton(Form)
        self.ToSecondTrainer.setGeometry(QtCore.QRect(100, 160, 199, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.ToSecondTrainer.sizePolicy().hasHeightForWidth())
        self.ToSecondTrainer.setSizePolicy(sizePolicy)
        self.ToSecondTrainer.setMinimumSize(QtCore.QSize(0, 50))
        self.ToSecondTrainer.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.ToSecondTrainer.setFont(font)
        self.ToSecondTrainer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ToSecondTrainer.setStyleSheet("QPushButton {\n"
"  rgb(170, 255, 127);\n"
"}\n"
"")
        self.ToSecondTrainer.setIconSize(QtCore.QSize(20, 20))
        self.ToSecondTrainer.setObjectName("ToSecondTrainer")
        self.ToFirstTrainer = QtWidgets.QPushButton(Form)
        self.ToFirstTrainer.setEnabled(True)
        self.ToFirstTrainer.setGeometry(QtCore.QRect(100, 70, 199, 50))
        self.ToFirstTrainer.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.ToFirstTrainer.setFont(font)
        self.ToFirstTrainer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ToFirstTrainer.setObjectName("ToFirstTrainer")
        self.Language = QtWidgets.QPushButton(Form)
        self.Language.setGeometry(QtCore.QRect(330, 20, 51, 41))
        self.Language.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Language.setText("")
        self.Language.setObjectName("Language")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ToSecondTrainer.setText(_translate("Form", "Второй тренажер"))
        self.ToFirstTrainer.setText(_translate("Form", "Первый тренажер"))
