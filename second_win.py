# напиши здесь код для второго экрана приложения
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt5.QtGui import QFont, QIcon, QPixmap

from instr import *
from final_win import *


class Experiment():
    def __init__(self, age, test1, test2, test3):
        self.age = age
        self.t1 = test1
        self.t2 = test2
        self.t3 = test3


class TestWin(QWidget):
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
        self.surname = QLabel(txt_surname)
        self.age = QLabel(txt_age)
        self.test1 = QLabel(txt_test1)
        self.test2 = QLabel(txt_test2)
        self.test3 = QLabel(txt_test3)
        self.text_timer = QLabel(text_timers)
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        # 
        self.button1 = QPushButton(txt_button1)
        self.button2 = QPushButton(txt_button2)
        self.button3 = QPushButton(txt_button3)
        self.button_result = QPushButton(txt_button_result)
        self.button1.setStyleSheet("background-color: rgb(255, 0, 51);")
        self.button2.setStyleSheet("background-color: rgb(255, 0, 51);")
        self.button3.setStyleSheet("background-color: rgb(255, 0, 51);")
        self.button_result.setStyleSheet("\n"
"font: 30 30pt \"Candara\";\n"
"color: rgb(248, 0, 0);\n"
"\n"
"\n"
"\n"
"\n"
"border-radius: 40;")
        # 
        self.line1 = QLineEdit()
        self.line2 = QLineEdit()
        self.line3 = QLineEdit()
        self.line4 = QLineEdit()
        self.line5 = QLineEdit()
        self.line1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line5.setStyleSheet("background-color: rgb(255, 255, 255);")
        # 
        self.v_line = QVBoxLayout()
        self.v_line2 = QVBoxLayout() 
        self.h_line = QHBoxLayout() 
        # 
        self.v_line.addWidget(self.surname, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.line1, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.age, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.line2, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.test1, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.button1, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.line3, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.test2, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.button2, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.test3, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.button3, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.line4, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.line5, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.button_result, alignment = Qt.AlignCenter)
        # 
        self.v_line2.addWidget(self.text_timer, alignment = Qt.AlignRight)
        #    
        self.h_line.addLayout(self.v_line)
        self.h_line.addLayout(self.v_line2)
        self.setLayout(self.h_line)
    def timer_test(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer_sits(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        #одно приседание в 1.5 секунды
        self.timer.start(1500)

    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer_final(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)
    
    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        else:
            self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
        
    def connects(self):
        self.button1.clicked.connect(self.timer_test)
        self.button2.clicked.connect(self.timer_sits)
        self.button3.clicked.connect(self.timer_final)
        self.button_result.clicked.connect(self.next_click)
 
    def next_click(self):
        self.hide()
        self.exp = Experiment(self.line2.text(), self.line3.text(), self.line4.text(), self.line5.text())
        self.tw = FinalWin(self.exp)
