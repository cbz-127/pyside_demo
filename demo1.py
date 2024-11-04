from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit

import sys

class myWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # btn = QPushButton('let go to push it', self)
        ql = QLineEdit(self)
        ql.setPlaceholderText('please input you password')

if __name__ == '__main__':
    app = QApplication([])
    mv = myWindow()
    mv.show()
    sys.exit(app.exec())    
    