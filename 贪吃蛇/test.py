from PyQt5.QtCore import Qt
from PyQt5.QtGui import*
from PyQt5.QtGui import QPaintEvent
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
import sys

from PyQt5.QtWidgets import QWidget

class SnakeGame(QMainWindow):#引用QMainWindow创建窗口
    def __init__(self):
        super().__init__()
        #设置窗口大小
        self.setWindowTitle("贪吃蛇小游戏")
        self.resize(640, 480)
        self.setWindowIcon(QIcon("./img/icon.png"))
        #创建框架
        self.frame = GameFrame(self)
        #设置到当前窗口
        self.setCentralWidget(self.frame)
        
class GameFrame(QFrame):
    def __init__(self, parent: QWidget):
        super().__init__(parent)
        
        
    #创建画框
    def paintEvent(self, a0: QPaintEvent):
        # return super().paintEvent(a0)
        #创建画笔
        painter = QPainter(self)
        painter.set
        
        
        
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = SnakeGame()
    game.show()
    sys.exit(app.exec_())
    