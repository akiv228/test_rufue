from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QPushButton, QWidget, QLabel, 
QVBoxLayout)
from PyQt5.QtGui import QFont, QIcon, QPixmap, QIntValidator

from config import *
from test1 import *
from unacceptable_age import *

class Acquaintance(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(title)
        self.resize(win_width, win_height)
        self.setMaximumSize(win_width, win_height)
        self.move(win_x, win_y)
        self.setStyleSheet("background-color: rgb(255, 255, 122);")
        self.icon = QIcon()
        self.icon.addPixmap(QPixmap("images/health2.png"), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(self.icon)


    def initUI(self):
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("images/line.png").scaled(720, 170))
        
        self.surname = QLabel(txt_surname)
        self.surname.setFont(QFont("Times", 23))
        
        self.age = QLabel(txt_age)
        self.age.setFont(QFont("Times", 23))
        
        self.line1 = QLineEdit()
        self.line1.setFixedWidth(250)
        self.line1.setFont(QFont('Arial', 15))
        self.line1.setStyleSheet("background-color: rgb(255, 255, 255);")
        
        self.line2 = QLineEdit()
        self.line2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line2.setFixedWidth(250)
        self.line2.setFont(QFont('Arial', 15))
        
        self.but_start = QPushButton(txt_but_manual)
        self.but_start.setStyleSheet("font: 50 50pt \"Candara\"; color: rgb(248, 0, 0); border-radius: 40;")
        
        self.v_line = QVBoxLayout()
        self.v_line.addWidget(self.label, alignment = Qt.AlignCenter)
        self.v_line.addWidget(self.surname, alignment = Qt.AlignCenter)
        self.v_line.addWidget(self.line1, alignment = Qt.AlignCenter)
        self.v_line.addWidget(self.age, alignment = Qt.AlignCenter)
        self.v_line.addWidget(self.line2, alignment = Qt.AlignCenter)
        self.v_line.addWidget(self.but_start, alignment = Qt.AlignCenter)
        self.setLayout(self.v_line)
        
        self.line2.setValidator(QIntValidator(7, 99))
        
        self.msgBox = QMessageBox()
        self.msgBox.setIcon(QMessageBox.Critical)
        self.msgBox.setWindowIcon(self.icon)
        self.msgBox.setWindowTitle("Ошибка!")
        self.msgBox.setStyleSheet(
        "QMessageBox {background:rgb(255, 221, 51);}"
        "QPushButton {color:black; font-family:Arial; font-size:15px; background-color:rgb(248, 0, 0);}")


    def connects(self):
        self.but_start.clicked.connect(self.next_click)
        

    def next_click(self):
        age_validator = QIntValidator(7, 85)
        if len(self.line1.text()) == 0:
            self.msgBox.setText(warning_tecst)
            self.msgBox.show()
        elif age_validator.validate(self.line2.text(), 0)[0] != 2:
            # self.msgBox.setText(warning_age)
            # self.msgBox.show()
            self.hide()
            self.tw = Unacceptable_age()
        else:
            self.hide()
            self.tw = Test1(self.line2.text())
        # self.hide()
        # self.tw = Test1(self.line2.text())
