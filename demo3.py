################################################################################
## 
## 计算器
## 
################################################################################
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QVBoxLayout,QWidget
from Ui_Calculator import Ui_Form

import sys

class myWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.str = ''
        self.nums = []
        self.mid_result = 0
        self.pushButton_0.clicked.connect(lambda: self.showNum('0'))
        self.pushButton_1.clicked.connect(lambda: self.showNum('1'))
        self.pushButton_2.clicked.connect(lambda: self.showNum('2'))
        self.pushButton_3.clicked.connect(lambda: self.showNum('3'))
        self.pushButton_4.clicked.connect(lambda: self.showNum('4'))
        self.pushButton_5.clicked.connect(lambda: self.showNum('5'))
        self.pushButton_6.clicked.connect(lambda: self.showNum('6'))
        self.pushButton_7.clicked.connect(lambda: self.showNum('7'))
        self.pushButton_8.clicked.connect(lambda: self.showNum('8'))
        self.pushButton_9.clicked.connect(lambda: self.showNum('9'))
        self.pushButton_point.clicked.connect(lambda: self.showNum('.'))
        self.pushButton_add.clicked.connect(lambda: self.comput('+'))
        self.pushButton_sub.clicked.connect(lambda: self.comput('-'))
        self.pushButton_mul.clicked.connect(lambda: self.comput('*'))
        self.pushButton_div.clicked.connect(lambda: self.comput('/'))
        self.pushButton_equal.clicked.connect(self.comput)
    
    def showNum(self,num):
        self.nums.append(num)
        self.lineEdit.clear()
        self.str = self.str + num
        self.lineEdit.setText(self.str)
        #print(self.str)
    def comput(self):
        print(self.nums)
    
    
        
if __name__ == '__main__':
    app = QApplication([])
    mv = myWindow()
    mv.show()
    sys.exit(app.exec())  
    # app.exec()