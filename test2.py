from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QMessageBox
from PyQt5.QtGui import QFont, QIcon, QPixmap, QIntValidator

from config import *
from test3 import *


class Test2(QWidget):
    def __init__(self, age, t1):
        self.age = age
        self.t1 = t1
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
        self.sound = QSound('audio/squats.wav', self) 
        
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("images/line.png").scaled(750, 160))
        
        self.test2 = QLabel(txt_test2)
        self.test2.setFont(QFont("Times", 20))
        
        self.test_h = QLabel(txt_help)
        self.test_h.setFont(QFont("Times", 15,  QFont.Bold))
        self.test_h.setStyleSheet("font: bold italic;")
        
        self.text_timer = QLabel(text_timers2)
        self.text_timer.setFont(QFont("Times", 45, QFont.Bold))
        
        self.button2 = QPushButton(txt_button2)
        self.button2.setStyleSheet(
"QPushButton {background-color : red; font: 20 20pt \"Candara\";}"
"QPushButton::pressed {background-color : lightgreen; font: 20 20pt \"Candara\";}")
        
        self.button_result  = QPushButton(txt_but_manual)
        self.button_result.setStyleSheet("font: 45 45pt \"Candara\"; color: rgb(248, 0, 0); border-radius: 40;")
        
        self.v_line = QVBoxLayout()
        self.v_line2 = QVBoxLayout() 
        self.h_line = QHBoxLayout() 
        
        self.v_line.addWidget(self.label, alignment = Qt.AlignRight)
        self.v_line.addWidget(self.test2, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.test_h, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.button2, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.button_result, alignment = Qt.AlignCenter)
        
        self.v_line2.addWidget(self.text_timer, alignment = Qt.AlignRight)
          
        self.h_line.addLayout(self.v_line)
        self.h_line.addLayout(self.v_line2)
        self.setLayout(self.h_line)
        
        self.msgBox = QMessageBox()
        self.msgBox.setIcon(QMessageBox.Critical)
        self.msgBox.setWindowIcon(self.icon)
        self.msgBox.setWindowTitle("Ошибка!")
        self.msgBox.setStyleSheet(
        "QMessageBox {background:rgb(255, 221, 51);}"
        "QPushButton {color:black; font-family:Arial; font-size:15px; background-color:rgb(248, 0, 0);}")
        
        
    def timer_sits(self):
        global time2
        time2 = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        #одно приседание в 1.5 секунды
        self.timer.start(1500)
        self.sound.play()
        self.button_result.clicked.connect(self.button_result_event)

    def timer2Event(self):
        global time2
        time2 = time2.addSecs(-1)
        self.text_timer.setText(time2.toString("hh:mm:ss")[6:8])
        self.text_timer.setFont(QFont("Times", 45, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time2.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
            self.sound.stop()


    def button_result_event(self):
        if self.timer.isActive():
            self.warning()
        else:
            self.next_click()
    
    def warning(self):
        self.msgBox.setText(warning_timer)
        self.msgBox.show()


    def connects(self):
        self.button2.clicked.connect(self.timer_sits)
        # self.button_result.clicked.connect(self.next_click)
 
    def next_click(self):
        self.hide()
        self.tw = Test3(self.age, self.t1)
