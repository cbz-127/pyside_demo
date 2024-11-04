from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QVBoxLayout,QWidget

import sys

class myWindow(QWidget):
    def __init__(self):
        super().__init__()
        mainLayout = QVBoxLayout()
           
        btn = QPushButton('按钮')
        # 按钮点击信号
        btn.clicked.connect(self.hello)

        mainLayout.addWidget(btn)

        self.setLayout(mainLayout)

    def hello(self):
        print('hello')
        
if __name__ == '__main__':
    app = QApplication([])
    mv = myWindow()
    mv.show()
    sys.exit(app.exec())    
    