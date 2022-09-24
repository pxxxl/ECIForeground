import random
import copy

from PySide6.QtCore import(
    QSize
)
from PySide6.QtWidgets import(
    QApplication,
    
)

from MainWindow import *

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()