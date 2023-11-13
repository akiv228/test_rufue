from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QPushButton, QWidget, QLabel,
                             QVBoxLayout)
from PyQt5.QtGui import QFont, QIcon, QPixmap

from config import *



class Unacceptable_age(QWidget):
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
        self.label.setPixmap(QPixmap("images/line.png").scaled(720, 170))
        
        self.welcome = QLabel(title_attention)
        self.welcome.setFont(QFont("Times", 27, QFont.Bold))
        
        self.description = QLabel(txt_age2)
        self.description.setFont(QFont("Times", 23))
        
        self.goodbye = QLabel(txt_love)
        self.goodbye.setFont(QFont("Times", 17))
        
        self.but_start = QPushButton(txt_end)
        self.but_start.setStyleSheet("font: 45pt \"Candara\"; color: rgb(248, 0, 0); border-radius: 40;")
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.welcome, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.description, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.goodbye, alignment=Qt.AlignRight)
        self.layout.addWidget(self.but_start, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)

    def connects(self):
        self.but_start.clicked.connect(self.next_click)

    def next_click(self):
        self.close()
        # self.tw = Acquaintance()
