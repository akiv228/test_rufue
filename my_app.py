from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QPushButton, QWidget, QLabel, 
QVBoxLayout, QHBoxLayout)
from PyQt5.QtGui import QFont, QIcon, QPixmap

from config import *
from instruc import *
from acquaintance import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
        self.setStyleSheet("background-color: rgb(255, 255, 122);")
        icon = QIcon()
        icon.addPixmap(QPixmap("images/health2.png"), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.setMaximumSize(win_width, win_height)
        

    def initUI(self):
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("images/phone2.png").scaledToHeight(410))
        
        self.welcome = QLabel(txt_welcome)
        self.welcome.setFont(QFont("Times", 20, QFont.Bold))
        
        self.but_start = QPushButton(txt_but_start)
        self.but_start.setStyleSheet("font: 60pt \"Candara\"; color: rgb(248, 0, 0); border-radius: 40;")
        
        self.layout = QVBoxLayout() 
        self.layout.addWidget(self.welcome, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.label, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.but_start, alignment = Qt.AlignCenter)
        self.setLayout(self.layout)

    def connects(self):
        self.but_start.clicked.connect(self.next_click)
        
    def next_click(self):
        self.hide()
        # self.tw = Acquaintance()
        self.tw = Manual()


app = QApplication([])
window = MainWindow()   
app.exec()