# напиши здесь код основного приложения и первого экрана
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QPushButton, QWidget, QLabel, 
QVBoxLayout, QHBoxLayout)
from PyQt5.QtGui import QFont, QIcon, QPixmap

# https://github.com/algogrodno/pygame_star_aliens.git
from instr import *
from second_win import *


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
        icon.addPixmap(QPixmap("health2.png"), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

    def initUI(self):
        self.welcome = QLabel(txt_welcome)
        self.welcome.setFont(QFont("Times", 18, QFont.Bold))
        self.description = QLabel(txt_description)
        self.description.setFont(QFont("Times", 12))
        self.but_start = QPushButton(txt_but_start)
        self.but_start.setStyleSheet("\n"
"font: 75 60pt \"Candara\";\n"
"color: rgb(248, 0, 0);\n"
"\n"
"\n"
"\n"
"\n"
"border-radius: 40;")
        self.layout = QVBoxLayout() 
        self.layout.addWidget(self.welcome, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.description, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.but_start, alignment = Qt.AlignCenter)
        self.setLayout(self.layout)

    def connects(self):
        self.but_start.clicked.connect(self.next_click)
        
    def next_click(self):
        self.hide()
        self.tw = TestWin()


app = QApplication([])
window = MainWindow()   
app.exec()