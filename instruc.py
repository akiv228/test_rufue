from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QMessageBox
from PyQt5.QtGui import QFont, QIcon, QPixmap, QIntValidator
from config import *
from warning import *



class Manual(QWidget):
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
        self.sound = QSound('audio/squats.wav', self)
        
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("images/line.png").scaled(730, 170))
        
        self.welcome = QLabel(title_manual)
        self.welcome.setFont(QFont("Times", 25, QFont.Bold))
        
        self.description = QLabel(txt_description)
        self.description.setFont(QFont("Times", 15))
        
        self.but_start = QPushButton(txt_but_manual)
        self.but_start.setStyleSheet("font: 50pt \"Candara\"; color: rgb(248, 0, 0); border-radius: 40;")
        
        self.but_sound = QPushButton(txt_but_manual)
        self.but_sound.setStyleSheet("font: 50pt \"Candara\"; color: rgb(248, 0, 0); border-radius: 40;")
        
        self.layout = QVBoxLayout()
        # self.layout.addWidget(self.but_sound, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.label, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.welcome, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.description, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.but_start, alignment = Qt.AlignCenter)
        self.setLayout(self.layout)



    def connects(self):
        self.but_start.clicked.connect(self.next_click)
        # self.but_sound.clicked.connect(self.sounds)

    # def sounds(self):
    #     self.playing = True
    #     if self.playing:
    #         self.sound.play()
    #         self.playing = False
    #     if not self.playin

    def next_click(self):
        self.hide()
        self.tw = Warning()
