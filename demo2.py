################################################################################
## 
## 登录功能
## 
################################################################################
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QVBoxLayout,QWidget
from Ui_LoginWindow import Ui_Form

import sys

class myWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login)
    
    def login(self):
        if self.lineEdit.text() == 'cbz' and self.lineEdit_2.text() == '123':
            print('login success')
        else:
            print('login fail')
    
    
        
if __name__ == '__main__':
    app = QApplication([])
    mv = myWindow()
    mv.show()
    sys.exit(app.exec())  
    # app.exec()