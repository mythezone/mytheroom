
import sys 
from PySide6.QtWidgets import QApplication, QLabel, QWidget

app = QApplication(sys.argv)

print(sys.argv)

window = QWidget()
window.show()

app.exec()