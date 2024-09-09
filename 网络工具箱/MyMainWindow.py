from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

from PyQt5.QtWidgets import QWidget
from Ui_MyWin import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #加载UI内容
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.init_ui()
        
    # def init_ui(self):
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
        