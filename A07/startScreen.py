# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'A07.ui'
#
# Created: Sat Feb 28 21:20:30 2015
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
from A07.res import *

# HINWEIS: Ui_MainWindow muss von QMainWindow erben nicht von "object"!
from A07.sphere import Sphere


class Ui_MainWindow(QMainWindow):
    def __init__(self, parent=None):
        """
        Konstruktor
        :param parent:
        """
        super().__init__(parent)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        """
        ERSTELLT DIE GUI
        :param MainWindow:
        :return:
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/A07 Splash Screen Version 3.jpg"))
        self.label.setContentsMargins(0, 0, 0, 0)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.start_Button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.start_Button.sizePolicy().hasHeightForWidth())
        self.start_Button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.start_Button.setFont(font)
        self.start_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_Button.setDefault(False)
        self.start_Button.setFlat(True)
        self.start_Button.setObjectName("start_Button")
        self.verticalLayout.addWidget(self.start_Button)
        self.tutorial_Button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tutorial_Button.sizePolicy().hasHeightForWidth())
        self.tutorial_Button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(False)
        font.setUnderline(True)
        self.tutorial_Button.setFont(font)
        self.tutorial_Button.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.tutorial_Button.setDefault(True)
        self.tutorial_Button.setFlat(True)
        self.tutorial_Button.setObjectName("tutorial_Button")
        self.verticalLayout.addWidget(self.tutorial_Button)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 21))
        self.menubar.setObjectName("menubar")
        self.menuA07 = QtWidgets.QMenu(self.menubar)
        self.menuA07.setObjectName("menuA07")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuA07.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Welcome to our Solarsystem"))
        # Titel
        self.menuA07.setTitle(_translate("MainWindow", "A07"))

        # Button text
        self.start_Button.setText(_translate("MainWindow", "START"))
        self.tutorial_Button.setText(_translate("MainWindow", "TUTORIAL"))

        self.start_Button.clicked.connect(self.starteGUI)


    def starteGUI(self):
        self.close()
        s = Sphere()
        s.main()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = Ui_MainWindow() #CREATE - VIEW
    view.show()            #SHOW - View
    sys.exit(app.exec_())  #EXECUTE Funktionen



