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
        self.ToSecondTrainer.setGeometry(QtCore.QRect(120, 180, 131, 51))
        self.ToSecondTrainer.setObjectName("ToSecondTrainer")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(290, 20, 73, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ToSecondTrainer.setText(_translate("Form", "Второй тренажер"))
        self.comboBox.setCurrentText(_translate("Form", "Русский"))
        self.comboBox.setItemText(0, _translate("Form", "Русский"))
        self.comboBox.setItemText(1, _translate("Form", "English"))
