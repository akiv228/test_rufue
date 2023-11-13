from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont, QIcon, QPixmap


from config import *


class FinalWin(QWidget):
    def __init__(self, age, t1, t2, t3):
        # self.exp = exp
        self.age = age
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()

    def results(self):
        self.index = (4*(int(self.t1)+int(self.t2)+int(self.t3))-200)/10
        if self.index <= 0:
            return txt_mistake
        if int(self.age) >= 15:
            if self.index >= 15:
                return txt_res1
            elif self.index < 15 and self.index >= 11:
                return txt_res2
            elif self.index < 11 and self.index >= 6:
                return txt_res3
            elif self.index < 6 and self.index >= 0.5:
                return txt_res4
            elif self.index <= 0.4:
                return txt_res5
        
        elif int(self.age) == 14 or int(self.age) == 13:
            if self.index >= 16.5:
                return txt_res1
            elif self.index < 16.5 and self.index >= 12.5:
                return txt_res2
            elif self.index < 12.5 and self.index >= 7.5:
                return txt_res3
            elif self.index < 7.5 and self.index >= 2:
                return txt_res4
            elif self.index <= 2:
                return txt_res5
    
        elif int(self.age) == 11 or int(self.age) == 12:
            if self.index >= 18:
                return txt_res1
            elif self.index < 18 and self.index >= 14:
                return txt_res2
            elif self.index < 14 and self.index >= 9:
                return txt_res3
            elif self.index < 9 and self.index >= 3.5:
                return txt_res4
            elif self.index <= 3.5:
                return txt_res5
        
        elif int(self.age) == 9 or int(self.age) == 10:
            if self.index >= 19.5:
                return txt_res1
            elif self.index < 19.5 and self.index >= 15.5:
                return txt_res2
            elif self.index < 15.5 and self.index >= 10.5:
                return txt_res3
            elif self.index < 10.5 and self.index >= 5:
                return txt_res4
            elif self.index <= 5:
                return txt_res5
        
        elif int(self.age) == 7 or int(self.age) == 8:
            if self.index >= 21:
                return txt_res1
            elif self.index < 21 and self.index >= 17:
                return txt_res2
            elif self.index < 17 and self.index >= 12:
                return txt_res3
            elif self.index < 12 and self.index >= 6.5:
                return txt_res4
            elif self.index <= 6.5:
                return txt_res5

    def set_appear(self):
        self.setWindowTitle(title)
        self.resize(win_width, win_height)
        self.setMaximumSize(win_width, win_height)
        self.move(win_x, win_y)
        self.setStyleSheet("background-color: rgb(255, 255, 122);")
        icon = QIcon()
        icon.addPixmap(QPixmap("images/health2.png"), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

    def initUI(self):
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("images/line.png").scaled(750, 170))
        
        self.label_res = QLabel(self)
        # self.label_res.setPixmap(QPixmap("line_result.png").scaled(580, 180))
        
        self.result = QLabel(txt_result + self.results())
        self.result.setFont(QFont("Times", 22, QFont.Bold))
        
        self.rufindex = QLabel(txt_index + str(self.index))
        self.rufindex.setFont(QFont("Times", 22, QFont.Bold))
        
        self.advise = QLabel()
        self.advise.setFont(QFont("Times", 18))
        self.advise.setStyleSheet("font: italic;")
        
        if self.results() == txt_res5:
            self.label_res.setPixmap(QPixmap("images/line_result5.png").scaled(580, 180))
            self.advise.setText(advise5)
        elif self.results() == txt_res4:
            self.label_res.setPixmap(QPixmap("images/line_result4.png").scaled(580, 180))
            self.advise.setText(advise4)
        elif self.results() == txt_res3:
            self.label_res.setPixmap(QPixmap("images/line_result3.png").scaled(580, 180))
            self.advise.setText(advise3)
        elif self.results() == txt_res2:
            self.label_res.setPixmap(QPixmap("images/line_result2.png").scaled(580, 180))
            self.advise.setText(advise2)
        elif self.results() == txt_res1:
            self.label_res.setPixmap(QPixmap("images/line_result1.png").scaled(580, 180))
            self.advise.setText(advise1)
        elif self.results() == txt_mistake:
            self.label_res.setPixmap(QPixmap("images/line_result_mistake.png").scaled(580, 180))
            self.advise.setText(advise_mistake)
        
        self.v_line = QVBoxLayout() 
        self.v_line.addWidget(self.label, alignment = Qt.AlignCenter)
        self.v_line.addWidget(self.rufindex, alignment = Qt.AlignCenter)
        self.v_line.addWidget(self.result, alignment = Qt.AlignCenter)
        self.v_line.addWidget(self.label_res, alignment = Qt.AlignCenter)
        self.v_line.addWidget(self.advise, alignment = Qt.AlignCenter)
        self.setLayout(self.v_line)
