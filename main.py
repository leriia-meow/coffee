import sys

import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QPaintEvent, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
import sqlite3


class Ui_MainWindow5(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(348, 255)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 10, 171, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 40, 171, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(160, 70, 171, 22))
        self.comboBox.setObjectName("comboBox")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 100, 171, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 130, 171, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(160, 160, 171, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 101, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 101, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 130, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 160, 51, 16))
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 190, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 190, 131, 16))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 348, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Название сорта"))
        self.label_2.setText(_translate("MainWindow", "Степень обжарки"))
        self.label_3.setText(_translate("MainWindow", "Молотый/в зернах"))
        self.label_4.setText(_translate("MainWindow", "Описание вкуса"))
        self.label_5.setText(_translate("MainWindow", "Цена"))
        self.label_6.setText(_translate("MainWindow", "Объем"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))


class Ui_MainWindow6(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(348, 255)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 10, 171, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 40, 171, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(160, 70, 171, 22))
        self.comboBox.setObjectName("comboBox")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 100, 171, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 130, 171, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(160, 160, 171, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 101, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 101, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 130, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 160, 51, 16))
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 190, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 190, 131, 16))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 348, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Название сорта"))
        self.label_2.setText(_translate("MainWindow", "Степень обжарки"))
        self.label_3.setText(_translate("MainWindow", "Молотый/в зернах"))
        self.label_4.setText(_translate("MainWindow", "Описание вкуса"))
        self.label_5.setText(_translate("MainWindow", "Цена"))
        self.label_6.setText(_translate("MainWindow", "Объем"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("coffee")
        MainWindow.resize(427, 388)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 0, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(10, 25, 411, 331))
        self.tableView.setObjectName("tableView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 427, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 0, 131, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("coffee", "coffee"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_2.setText(_translate("MainWindow", "Редактировать"))


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.new)
        self.pushButton_2.clicked.connect(self.newf)
        self.tableView.clicked.connect(self.t)
        self.n = 0
        self.rez()

    def t(self, x):
        self.n = self.tableView.currentIndex().row()

    def rez(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffee.db')
        db.open()
        view = self.tableView
        model = QSqlTableModel(self, db)
        model.setTable('coffee')
        model.select()
        view.setModel(model)

    def new(self):
        self.win = Winn()
        self.win.show()
        self.win.pushButton.clicked.connect(self.rez)

    def newf(self):
        self.con = sqlite3.connect('coffee.db')
        self.cur = self.con.cursor()
        result = self.cur.execute('''SELECT * FROM coffee''').fetchall()
        self.win = Winnf(result[self.n][0])
        self.win.show()
        self.win.pushButton.clicked.connect(self.rez)


class Winnf(QMainWindow, Ui_MainWindow6):
    def __init__(self, a):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect('coffee.db')
        self.cur = self.con.cursor()
        self.g = self.cur.execute('''SELECT * FROM coffee WHERE ID = ?''', (a,)).fetchall()
        self.lineEdit.setText(self.g[0][1])
        self.lineEdit_2.setText(str(self.g[0][2]))
        self.lineEdit_3.setText(str(self.g[0][4]))
        self.lineEdit_4.setText(str(self.g[0][5]))
        self.lineEdit_5.setText(str(self.g[0][6]))
        self.pushButton.clicked.connect(self.do)
        for i in ["Молотый", "В зернах"]:
            self.comboBox.addItem(i)

    def do(self):
        self.label_7.setText("")
        a = self.lineEdit.text()
        b = self.lineEdit_2.text()
        c = self.lineEdit_3.text()
        d = self.comboBox.currentText()
        e = self.lineEdit_4.text()
        f = self.lineEdit_5.text()
        if a and b and c and e and f:
            try:
                e = float(e)
                f = float(e)
                if e >= 0 and f >= 0:
                    self.cur.execute("UPDATE coffee SET название = ?, степень = ?, молотость = ?, "
                                     "описание = ?, цена = ?, объем = ? WHERE id = ?",
                                     (a, b, c, d, e, f, self.g[0][0]))
                    self.con.commit()
                    self.close()
                else:
                    self.label_7.setText("Неверный формат ввода")
            except Exception:
                self.label_7.setText("Неверный формат ввода")
        else:
            self.label_7.setText("Неверный формат ввода")


class Winn(QMainWindow, Ui_MainWindow5):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect('coffee.db')
        self.cur = self.con.cursor()
        for i in ["Молотый", "В зернах"]:
            self.comboBox.addItem(i)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.label_7.setText("")
        a = self.lineEdit.text()
        b = self.lineEdit_2.text()
        c = self.lineEdit_3.text()
        d = self.comboBox.currentText()
        e = self.lineEdit.text()
        f = self.lineEdit.text()
        if a and b and c and e and f:
            try:
                e = float(e)
                f = float(e)
                if e >= 0 and f >= 0:
                    self.cur.execute("""INSERT INTO coffee(название, степень, молотость,
                                         описание, цена, объем) VALUES(?, ?, ?, ?, ?, ?)""",
                                     (a, b, c, d, e, f))
                    self.con.commit()
                    self.close()
                else:
                    self.label_7.setText("Неверный формат ввода")
            except Exception:
                self.label_7.setText("Неверный формат ввода")
        else:
            self.label_7.setText("Неверный формат ввода")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wndw = Window()
    wndw.show()
    app.exec()
