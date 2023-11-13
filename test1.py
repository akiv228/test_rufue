from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QPushButton, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QMessageBox
from PyQt5.QtGui import QFont, QIcon, QPixmap, QIntValidator
from PyQt5.QtMultimedia import QSound

from config import *
from unacceptable_pulse import *
from test2 import *
# counts = 0

class Test1(QWidget):
    def __init__(self, age):
        self.age = age
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
        self.sound = QSound('audio/timer.wav', self) 
        self.sound2 = QSound('audio/end.wav', self) 
        
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("images/phone3.png").scaled(label_size_w, size_h))
        
        self.test1 = QLabel(txt_test1)
        self.test1.setFont(QFont("Times", 20))
        
        self.text_timer = QLabel(text_timers)
        self.text_timer.setFont(QFont("Times", 38, QFont.Bold))
         
        self.button1 = QPushButton(txt_button1)
        self.button1.setStyleSheet(
"QPushButton {background-color : red; font: 20 20pt \"Candara\";}"
"QPushButton::pressed {background-color : lightgreen; font: 20 20pt \"Candara\";}")
        
        self.button_result  = QPushButton(txt_but_manual)
        self.button_result.setStyleSheet("font: 45 45pt \"Candara\"; color: rgb(248, 0, 0); border-radius: 40;")
        
        self.line3 = QLineEdit()
        self.line3.setPlaceholderText("Ваш пульс")
        self.line3.setFixedWidth(300)
        self.line3.setFont(QFont('Arial', 15))
        self.line3.setStyleSheet("background-color: rgb(255, 255, 255);")
        
        self.v_line = QVBoxLayout()
        self.v_line2 = QVBoxLayout() 
        self.h_line = QHBoxLayout() 
        
        self.v_line.addWidget(self.test1, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.label, alignment = Qt.AlignCenter)
        self.v_line.addWidget(self.line3, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.button1, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.button_result, alignment = Qt.AlignCenter)
        
        self.v_line2.addWidget(self.text_timer, alignment = Qt.AlignRight)
          
        self.h_line.addLayout(self.v_line)
        self.h_line.addLayout(self.v_line2)
        self.setLayout(self.h_line)

        self.line3.setValidator(QIntValidator(7, 99))
        
        self.msgBox = QMessageBox()
        self.msgBox.setIcon(QMessageBox.Critical)
        self.msgBox.setWindowIcon(self.icon)
        self.msgBox.setWindowTitle("Ошибка!")
        self.msgBox.setStyleSheet(
        "QMessageBox {background:rgb(255, 221, 51);}"
        "QPushButton {color:black; font-family:Arial; font-size:15px; background-color:rgb(248, 0, 0);}")
    

    def timer_test(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
        
        self.sound.play()
        self.button_result.clicked.connect(self.button_result_event)
        
        

    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
            self.sound.stop()
            self.sound2.play()


    def button_result_event(self):
        if self.timer.isActive():
            self.warning()
        else:
            self.next_click()
    
    def warning(self):
        self.msgBox.setText(warning_timer)
        self.msgBox.show()

    def connects(self):
        # global counts
        self.button1.clicked.connect(self.timer_test)
        # if self.button1.clicked.connect(self.timer_test):
        #     counts += 1
        # if counts == 2:
        #     self.msgBox.setText(warning_timer)
        #     self.msgBox.show()
        # self.button_result.clicked.connect(self.next_click)

 
    def next_click(self):
        test_validator = QIntValidator(14, 35)
        if len(self.line3.text()) == 0:
            self.msgBox.setText(warning_line_edit)
            self.msgBox.show()
        elif test_validator.validate(self.line3.text(), 0)[0] != 2:
            self.hide()
            self.tw = Unacceptable_pulse()
            # self.msgBox.setText(warning_line_edit)
            # self.msgBox.show()
        else:
            self.hide()
            self.tw = Test2(self.age, self.line3.text())
