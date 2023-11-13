from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QMessageBox
from PyQt5.QtGui import QFont, QIcon, QPixmap, QIntValidator
from PyQt5.QtMultimedia import QSound
from unacceptable_pulse import *

from config import *
from final_win import *



class Test3(QWidget):
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
        self.sound = QSound('audio/timer.wav', self) 
        self.sound2 = QSound('audio/end.wav', self) 
        
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("images/phone3.png").scaled(label_size_w, size_h))
        
        self.test3 = QLabel(txt_test3)
        self.test3.setFont(QFont("Times", 20))
        
        self.test_h = QLabel(txt_help2)
        self.test_h.setFont(QFont("Times", 15,  QFont.Bold))
        self.test_h.setStyleSheet("font: bold italic;")
        
        self.text_timer = QLabel(text_timers3)
        self.text_timer.setFont(QFont("Times", 38, QFont.Bold))
        
        self.button3 = QPushButton(txt_button3)
        self.button3.setStyleSheet(
"QPushButton {background-color : red; font: 20 20pt \"Candara\";}"
"QPushButton::pressed {background-color : lightgreen; font: 20 20pt \"Candara\";}")
        
        self.button_result = QPushButton(txt_button_result)
        self.button_result.setStyleSheet("font: 30 30pt \"Candara\"; color: rgb(248, 0, 0); border-radius: 40;")
        
        self.line4 = QLineEdit()
        self.line4.setPlaceholderText("Ваш пульс за 1-ые 15 сек")
        self.line4.setFixedWidth(350)
        self.line4.setFont(QFont('Arial', 15))
        self.line4.setStyleSheet("background-color: rgb(255, 255, 255);")
        
        self.line5 = QLineEdit()
        self.line5.setPlaceholderText("Пульс за последние 15 сек")
        self.line5.setFixedWidth(350)
        self.line5.setFont(QFont('Arial', 15))
        self.line5.setStyleSheet("background-color: rgb(255, 255, 255);")
        
        self.v_line = QVBoxLayout()
        self.v_line2 = QVBoxLayout() 
        self.h_line = QHBoxLayout() 
        
        self.v_line.addWidget(self.test3, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.test_h, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.label, alignment = Qt.AlignCenter)
        self.v_line.addWidget(self.line4, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.line5, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.button3, alignment = Qt.AlignLeft)
        self.v_line.addWidget(self.button_result, alignment = Qt.AlignRight)
        
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

    
        self.line4.setValidator(QIntValidator(7, 99))
        self.line5.setValidator(QIntValidator(7, 99))
    
    def timer_final(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)
        # self.sound.play()
        self.button_result.clicked.connect(self.button_result_event)
    
    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 38, QFont.Bold))
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.sound.play()
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.sound.play()
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        else:
            self.text_timer.setStyleSheet("color: rgb(0,0,0)")
            self.sound.stop()
        if time.toString("hh:mm:ss") == "00:00:00":
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
        self.button3.clicked.connect(self.timer_final)

 
    def next_click(self):
        test_validator = QIntValidator(14, 55)
        # if test_validator.validate(self.line4.text(), 0)[0] != 2 or test_validator.validate(self.line5.text(), 0)[0] != 2:
        #     self.msgBox.setText(warning_line_edit)
        #     self.msgBox.show()
        # else:
        #     self.hide()
        #     self.tw = FinalWin(self.age, self.t1, self.line4.text(), self.line5.text())

        if len(self.line4.text()) == 0 or len(self.line5.text()) == 0:
            self.msgBox.setText(warning_line_edit)
            self.msgBox.show()
        elif test_validator.validate(self.line4.text(), 0)[0] != 2 or test_validator.validate(self.line5.text(), 0)[0] != 2:
            self.hide()
            self.tw = Unacceptable_pulse()
            # self.msgBox.setText(warning_line_edit)
            # self.msgBox.show()
        else:
            self.hide()
            self.tw = FinalWin(self.age, self.t1, self.line4.text(), self.line5.text())
