# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainMenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainMenu(object):
    def setupUi(self, mainMenu):
        mainMenu.setObjectName("mainMenu")
        mainMenu.resize(400, 500)
        mainMenu.setMinimumSize(QtCore.QSize(400, 500))
        mainMenu.setMaximumSize(QtCore.QSize(400, 500))
        self.verticalLayoutWidget = QtWidgets.QWidget(mainMenu)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 90, 341, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.avalibleScriptsButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.avalibleScriptsButton.setObjectName("avalibleScriptsButton")
        self.verticalLayout.addWidget(self.avalibleScriptsButton)
        self.viewRatingsButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.viewRatingsButton.setObjectName("viewRatingsButton")
        self.verticalLayout.addWidget(self.viewRatingsButton)
        self.settingsButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.settingsButton.setObjectName("settingsButton")
        self.verticalLayout.addWidget(self.settingsButton)

        self.retranslateUi(mainMenu)
        QtCore.QMetaObject.connectSlotsByName(mainMenu)

    def retranslateUi(self, mainMenu):
        _translate = QtCore.QCoreApplication.translate
        mainMenu.setWindowTitle(_translate("mainMenu", "Form"))
        self.avalibleScriptsButton.setText(_translate("mainMenu", "Доступные скрипты"))
        self.viewRatingsButton.setText(_translate("mainMenu", "Просмотр оценок пользователей"))
        self.settingsButton.setText(_translate("mainMenu", "Настройки"))