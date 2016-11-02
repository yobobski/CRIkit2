# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_PlotEffect_MergeNRBs.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(752, 260)
        Form.setStyleSheet("font: 10pt \"Arial\";")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBoxKK = QtWidgets.QGroupBox(Form)
        self.groupBoxKK.setObjectName("groupBoxKK")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBoxKK)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.comboBoxScaleLeftRight = QtWidgets.QComboBox(self.groupBoxKK)
        self.comboBoxScaleLeftRight.setObjectName("comboBoxScaleLeftRight")
        self.comboBoxScaleLeftRight.addItem("")
        self.comboBoxScaleLeftRight.addItem("")
        self.comboBoxScaleLeftRight.addItem("")
        self.verticalLayout_4.addWidget(self.comboBoxScaleLeftRight)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.label_6 = QtWidgets.QLabel(self.groupBoxKK)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.spinBoxWN = QtWidgets.QDoubleSpinBox(self.groupBoxKK)
        self.spinBoxWN.setMinimum(-10000.0)
        self.spinBoxWN.setMaximum(10000.0)
        self.spinBoxWN.setProperty("value", 3000.0)
        self.spinBoxWN.setObjectName("spinBoxWN")
        self.verticalLayout_4.addWidget(self.spinBoxWN)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.label_7 = QtWidgets.QLabel(self.groupBoxKK)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.spinBoxPix = QtWidgets.QSpinBox(self.groupBoxKK)
        self.spinBoxPix.setMinimum(-10000)
        self.spinBoxPix.setMaximum(10000)
        self.spinBoxPix.setProperty("value", 1400)
        self.spinBoxPix.setObjectName("spinBoxPix")
        self.verticalLayout_4.addWidget(self.spinBoxPix)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.horizontalLayout.addWidget(self.groupBoxKK)
        self.groupBoxMerge = QtWidgets.QGroupBox(Form)
        self.groupBoxMerge.setObjectName("groupBoxMerge")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBoxMerge)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayoutKK = QtWidgets.QHBoxLayout()
        self.horizontalLayoutKK.setObjectName("horizontalLayoutKK")
        self.horizontalLayout_2.addLayout(self.horizontalLayoutKK)
        self.horizontalLayout.addWidget(self.groupBoxMerge)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBoxKK.setTitle(_translate("Form", "Merge Parameters"))
        self.comboBoxScaleLeftRight.setItemText(0, _translate("Form", "Scale Left NRB"))
        self.comboBoxScaleLeftRight.setItemText(1, _translate("Form", "Scale Right NRB"))
        self.comboBoxScaleLeftRight.setItemText(2, _translate("Form", "None"))
        self.label_6.setText(_translate("Form", "Wavenumber"))
        self.label_7.setText(_translate("Form", "Pixel Number"))
        self.groupBoxMerge.setTitle(_translate("Form", "KK Parameters"))
