from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import sys

class ImageDisplay(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

    def set_image(self, image_path):
        pixmap = QPixmap(image_path)
        self.label.setPixmap(pixmap)