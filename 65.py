# PyQt5 images

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)

        label = QLabel(self)
        label.setGeometry(0, 0, 250, 250)

        pixmap = QPixmap(r"C:\Users\Kiran T\OneDrive\Pictures\Screenshots\Screenshot 2026-04-03 185901.png")
        label.setPixmap(pixmap)

        label.setScaledContents(True)

        label.setGeometry(self.width() - label.width(),
                        self.height() - label.height() , 
                        label.width(), 
                        label.height())

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
