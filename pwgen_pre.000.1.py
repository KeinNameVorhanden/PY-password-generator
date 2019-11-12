# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore, QtWidgets, QtGui
import random
import string
import sys


class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(220, 280)
        MainWindow.setStyleSheet("background: rgb(25, 25, 25)")
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_gen = QtWidgets.QPushButton(self.centralwidget)
        self.button_gen.setGeometry(QtCore.QRect(20, 90, 75, 20))
        self.button_gen.clicked.connect(self.generatePW)
        self.button_gen.setObjectName("button_gen")
        self.button_gen.setAutoFillBackground(False)
        self.button_gen.setStyleSheet("background: rgb(186, 186, 186)")
        self.label_pw = QtWidgets.QLabel(self.centralwidget)
        self.label_pw.setGeometry(QtCore.QRect(20, 20, 181, 31))
        self.label_pw.setFrameShape(QtWidgets.QFrame.Box)
        self.label_pw.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_pw.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pw.setStyleSheet("background: rgb(180, 180, 180)")
        self.label_pw.setObjectName("label_pw")
        self.counter_1 = QtWidgets.QSpinBox(self.centralwidget)
        self.counter_1.setGeometry(QtCore.QRect(160, 90, 40, 20))
        self.counter_1.setObjectName("counter_1")
        self.counter_1.setMinimum(int(1))
        self.counter_1.setMaximum(int(24))
        self.counter_1.setAutoFillBackground(False)
        self.counter_1.setStyleSheet("background: rgb(186, 186, 186)")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(20, 60, 70, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        self.radioButton.setPalette(palette)
        self.exitbtn = QtWidgets.QPushButton(self.centralwidget)
        self.exitbtn.setGeometry(QtCore.QRect(208, 0, 12, 12))
        self.exitbtn.clicked.connect(self.exitP)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.exitbtn.setPalette(palette)
        self.exitbtn.setObjectName("exitbtn")
        self.pwlist = QtWidgets.QListWidget(self.centralwidget)
        self.pwlist.setGeometry(QtCore.QRect(0, 120, 220, 160))
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        self.pwlist.setPalette(palette)
        self.pwlist.setObjectName("pwlist")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "000.2"))
        self.button_gen.setText(_translate("MainWindow", "GENERATE"))
        self.label_pw.setText(_translate("MainWindow", "Password"))
        self.radioButton.setText(_translate("btn_restrict", "SYMBOLS"))
        self.exitbtn.setText(_translate("MainWindow", "X"))
        self.counter_1.setValue(24)

    def generatePW(self):
        reynge = self.counter_1.value()
        if self.radioButton.isChecked():
            chars = string.ascii_letters + string.digits + '!@#$%^&*()'
        else:
            chars = string.ascii_letters + string.digits
        pw = ''.join(random.choice(chars) for i in range(reynge))
        self.label_pw.setText(pw)
        QApplication.clipboard().setText(pw)
        self.pwlist.addItem(pw)
        f = open("pw.txt", "a+")
        f.write(pw + "\n")

    def exitP(self):
        sys.exit(app.exec_())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
