import sys

import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QPaintEvent, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
import sqlite3
from addEditCoffeeForm import Ui_MainWindow6
from main import Ui_MainWindow


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
        db.setDatabaseName('data\coffee.db')
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
        self.con = sqlite3.connect('data\coffee.db')
        self.cur = self.con.cursor()
        result = self.cur.execute('''SELECT * FROM coffee''').fetchall()
        self.win = Winnf(result[self.n][0])
        self.win.show()
        self.win.pushButton.clicked.connect(self.rez)


class Winnf(QMainWindow, Ui_MainWindow6):
    def __init__(self, a):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect('data\coffee.db')
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


class Winn(QMainWindow, Ui_MainWindow6):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect('data\coffee.db')
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
