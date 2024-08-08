import sys 
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QMainWindow,QPushButton


from PySide6.QtCore import Qt, QSize    

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.the_button_is_checked = True 

        self.setWindowTitle("My App")
        # self.setFixedSize(QSize(400, 300))
        self.setMinimumSize(QSize(400, 300))
        self.setMaximumSize(QSize(800, 600))
        

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)

        
        button = QPushButton("Press me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)
        self.setCentralWidget(label)
        self.setCentralWidget(button)
        
        
    def the_button_was_clicked(self):
        print("Clicked!")
        
    def the_button_was_toggled(self, checked):
        self.the_button_is_checked = checked 
        print("Checked?", checked)
        
    
