# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'attempt2.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(602, 261)
        self.Name = QtWidgets.QGroupBox(Form)
        self.Name.setGeometry(QtCore.QRect(10, 9, 581, 241))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Name.setFont(font)
        self.Name.setAutoFillBackground(True)
        self.Name.setObjectName("Name")
        self.gridlayout = QtWidgets.QGridLayout(self.Name)
        self.gridlayout.setObjectName("gridlayout")
        self.Thing_2 = QtWidgets.QLabel(self.Name)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Thing_2.setFont(font)
        self.Thing_2.setAutoFillBackground(False)
        self.Thing_2.setObjectName("Thing_2")
        self.gridlayout.addWidget(self.Thing_2, 1, 0, 1, 1)
        self.Thing_3 = QtWidgets.QLabel(self.Name)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Thing_3.setFont(font)
        self.Thing_3.setAutoFillBackground(False)
        self.Thing_3.setObjectName("Thing_3")
        self.gridlayout.addWidget(self.Thing_3, 1, 2, 1, 1)
        self.Error = QtWidgets.QLabel(self.Name)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Error.setFont(font)
        self.Error.setAutoFillBackground(False)
        self.Error.setObjectName("Error")
        self.gridlayout.addWidget(self.Error, 0, 2, 1, 1)
        self.Thing_1 = QtWidgets.QLabel(self.Name)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Thing_1.setFont(font)
        self.Thing_1.setAutoFillBackground(False)
        self.Thing_1.setObjectName("Thing_1")
        self.gridlayout.addWidget(self.Thing_1, 0, 0, 1, 1)
        self.Value_1 = QtWidgets.QLabel(self.Name)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Value_1.setFont(font)
        self.Value_1.setAutoFillBackground(True)
        self.Value_1.setObjectName("Value_1")
        self.gridlayout.addWidget(self.Value_1, 0, 1, 1, 1)
        self.Value_5 = QtWidgets.QLabel(self.Name)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Value_5.setFont(font)
        self.Value_5.setAutoFillBackground(True)
        self.Value_5.setObjectName("Value_5")
        self.gridlayout.addWidget(self.Value_5, 0, 3, 1, 1)
        self.RefreshB = QtWidgets.QPushButton(self.Name)
        self.RefreshB.setObjectName("RefreshB")
        self.gridlayout.addWidget(self.RefreshB, 6, 3, 1, 1)
        self.Thing_7 = QtWidgets.QLabel(self.Name)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Thing_7.setFont(font)
        self.Thing_7.setAutoFillBackground(False)
        self.Thing_7.setObjectName("Thing_7")
        self.gridlayout.addWidget(self.Thing_7, 2, 2, 1, 1)
        self.Thing_6 = QtWidgets.QLabel(self.Name)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Thing_6.setFont(font)
        self.Thing_6.setAutoFillBackground(False)
        self.Thing_6.setObjectName("Thing_6")
        self.gridlayout.addWidget(self.Thing_6, 2, 0, 1, 1)
        self.Value_7 = QtWidgets.QLabel(self.Name)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Value_7.setFont(font)
        self.Value_7.setAutoFillBackground(True)
        self.Value_7.setObjectName("Value_7")
        self.gridlayout.addWidget(self.Value_7, 2, 3, 1, 1)
        self.Value_3 = QtWidgets.QLabel(self.Name)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Value_3.setFont(font)
        self.Value_3.setAutoFillBackground(True)
        self.Value_3.setObjectName("Value_3")
        self.gridlayout.addWidget(self.Value_3, 2, 1, 1, 1)
        self.Value_6 = QtWidgets.QLabel(self.Name)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Value_6.setFont(font)
        self.Value_6.setAutoFillBackground(True)
        self.Value_6.setObjectName("Value_6")
        self.gridlayout.addWidget(self.Value_6, 1, 3, 1, 1)
        self.Value_2 = QtWidgets.QLabel(self.Name)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Value_2.setFont(font)
        self.Value_2.setAutoFillBackground(True)
        self.Value_2.setObjectName("Value_2")
        self.gridlayout.addWidget(self.Value_2, 1, 1, 1, 1)
        self.Thing_10 = QtWidgets.QLabel(self.Name)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Thing_10.setFont(font)
        self.Thing_10.setAutoFillBackground(False)
        self.Thing_10.setObjectName("Thing_10")
        self.gridlayout.addWidget(self.Thing_10, 3, 0, 1, 1)
        self.Value_4 = QtWidgets.QLabel(self.Name)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Value_4.setFont(font)
        self.Value_4.setAutoFillBackground(True)
        self.Value_4.setObjectName("Value_4")
        self.gridlayout.addWidget(self.Value_4, 3, 1, 1, 1)
        self.Thing_12 = QtWidgets.QLabel(self.Name)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Thing_12.setFont(font)
        self.Thing_12.setAutoFillBackground(False)
        self.Thing_12.setObjectName("Thing_12")
        self.gridlayout.addWidget(self.Thing_12, 3, 2, 1, 1)
        self.Value_8 = QtWidgets.QLabel(self.Name)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Value_8.setFont(font)
        self.Value_8.setAutoFillBackground(True)
        self.Value_8.setObjectName("Value_8")
        self.gridlayout.addWidget(self.Value_8, 3, 3, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Name.setTitle(_translate("Form", "X"))
        self.Thing_2.setText(_translate("Form", "Y"))
        self.Thing_3.setText(_translate("Form", "Y"))
        self.Error.setText(_translate("Form", "K"))
        self.Thing_1.setText(_translate("Form", "Y"))
        self.Value_1.setText(_translate("Form", "Z"))
        self.Value_5.setText(_translate("Form", "P"))
        self.RefreshB.setText(_translate("Form", "Refresh"))
        self.Thing_7.setText(_translate("Form", "Y"))
        self.Thing_6.setText(_translate("Form", "Y"))
        self.Value_7.setText(_translate("Form", "Y"))
        self.Value_3.setText(_translate("Form", "Y"))
        self.Value_6.setText(_translate("Form", "Y"))
        self.Value_2.setText(_translate("Form", "Y"))
        self.Thing_10.setText(_translate("Form", "nope"))
        self.Value_4.setText(_translate("Form", "This is also going to be too LONGGGGGGGGGG"))
        self.Thing_12.setText(_translate("Form", "Y"))
        self.Value_8.setText(_translate("Form", "This is too long to fit in this box"))

