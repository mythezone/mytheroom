import sys 
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QMainWindow,QPushButton


from PySide6.QtCore import Qt, QSize    

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        # self.setFixedSize(QSize(400, 300))
        self.setMinimumSize(QSize(400, 300))
        self.setMaximumSize(QSize(800, 600))
        

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)

        
        button = QPushButton("Press me!")
        self.setCentralWidget(label)
        self.setCentralWidget(button)
        
