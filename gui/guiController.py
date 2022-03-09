import sys
from PyQt5.QtWidgets import *

from controller import searchController
from loadData import loadData
from gui.mainWindow import Ui_mainWindow
from gui.mainMenu import Ui_mainMenu
from gui.scriptsMenu import Ui_scriptsMenu
from searchAccounts import searchAccounts


class mainMenu(QWidget, Ui_mainMenu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class scriptsMenu(QWidget, Ui_scriptsMenu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class MainWindow(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # инициализация виджетов (экранов)
        self.mainMenu = mainMenu()
        self.scriptsMenu = scriptsMenu()
        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(self.mainMenu)
        self.stackedWidget.addWidget(self.scriptsMenu)
        self.setCentralWidget(self.stackedWidget)

        # функционал кнопок главного меню
        self.mainMenu.avalibleScriptsButton.clicked.connect(self.openScriptsMenu)
        #self.mainMenu.viewRatingsButton.clicked.connect(self.functionHere)
        #self.mainMenu.settingsButton.clicked.connect(self.functionHere)

        # функционал кнопок меня скриптов
        self.scriptsMenu.autoModeButton.clicked.connect(self.autoMode)
        #self.scriptsMenu.downloadProfilesButton.clicked.connect(self.functionHere)
        self.scriptsMenu.findNewAccountsButton.clicked.connect(self.findNewAccounts)
        #self.scriptsMenu.createRatingsFileButton.clicked.connect(self.functionHere)
        #self.scriptsMenu.cacheResetButton.clicked.connect(self.functionHere)
        #self.scriptsMenu.fileRepairButton.clicked.connect(self.functionHere)
        self.scriptsMenu.backButton.clicked.connect(self.openMainMenu)
        # временно
        self.stackedWidget.setCurrentWidget(self.mainMenu)

    def openScriptsMenu(self):
        self.stackedWidget.setCurrentWidget(self.scriptsMenu)

    def openMainMenu(self):
        self.stackedWidget.setCurrentWidget(self.mainMenu)

    def autoMode(self):
        controller=searchController(1, "no")

    def findNewAccounts(self):
        self.data = loadData()
        print("LoadData() отработал")
        self.data.loadAll()
        print("LoadAll() отработал")

        search = searchAccounts(self.data)
        search.runSearch("instbober", "$reset->name")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())