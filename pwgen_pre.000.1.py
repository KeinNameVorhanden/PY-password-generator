# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import random
import string


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(218, 135)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_gen = QtWidgets.QPushButton(self.centralwidget)
        self.button_gen.setGeometry(QtCore.QRect(20, 72, 75, 21))
        self.button_gen.clicked.connect(self.generatePW)
        self.button_gen.setObjectName("button_gen")
        self.label_pw = QtWidgets.QLabel(self.centralwidget)
        self.label_pw.setGeometry(QtCore.QRect(20, 20, 181, 31))
        self.label_pw.setFrameShape(QtWidgets.QFrame.Box)
        self.label_pw.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_pw.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pw.setObjectName("label_pw")
        self.counter_1 = QtWidgets.QSpinBox(self.centralwidget)
        self.counter_1.setGeometry(QtCore.QRect(155, 72, 45, 20))
        self.counter_1.setObjectName("counter_1")
        self.counter_1.setMaximum(int(24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 218, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password Gen - pre 000.1"))
        self.button_gen.setText(_translate("MainWindow", "GENERATE"))
        self.label_pw.setText(_translate("MainWindow", "Password"))
        self.counter_1.setValue(24)

    def generatePW(self):
        reynge = self.counter_1.value()
        chars = string.ascii_letters + string.digits
        pw = ''.join(random.choice(chars) for i in range(reynge))
        self.label_pw.setText(pw)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

