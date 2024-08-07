from component.container.main_window import MainWindow  
from PySide6.QtWidgets import QApplication
from PySide6 import QtWidgets, QtGui
import sys,os 

basedir = os.path.dirname(__file__)
try:
    from ctypes import windll  # Only exists on Windows.
    myappid = 'com.muiao.mytheroom'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(os.path.join(basedir,'asset/img/app.ico')))
    window = MainWindow()
    window.show()

    app.exec()