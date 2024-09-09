import random
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import *
from snake import Snake
from Food import Food

import sys

COLOR_BLACK = QColor(0, 0, 0)
COLOR_RED = QColor(255, 0, 0)
COLOR_GREEN = QColor(0, 255, 0)

SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
BLOCK_SIZE = 20  # 块大小
SCREEN_W = SCREEN_WIDTH // BLOCK_SIZE  # 32
SCREEN_H = SCREEN_HEIGHT // BLOCK_SIZE  # 24




# 创建窗口
class SnakeGame(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        # 设置窗口大小
        self.setWindowTitle("贪吃蛇游戏")
        # self.resize(640,480)
        self.setFixedSize(640, 480)  # 固定窗口大小
        # 创建画画板 QFrame                Frame:框架
        self.frame = GameFrame(self)  # 父容器
        # 设置到当前窗口里
        self.setCentralWidget(self.frame)



class GameFrame(QFrame):

    def __init__(self, parent: QWidget):
        super().__init__(parent)
        # 自动获取焦点
        self.setFocusPolicy(Qt.StrongFocus)
        self.init_game()

        # 开启定时器，根据一定间隔时间刷新界面
        self.timer = QTimer(self)  # 父容器
        self.timer.timeout.connect(self.update_game)  # 这里是传进来，并不是调用
        self.timer.start(200)
    
    def init_game(self):
        self.snake = Snake()
        # 苹果的位置
        self.food = Food(self.snake)
        
        
    # 刷新界面时，根据移动坐标更改蛇的位置
    def update_game(self):

        self.snake.move()
        
        head = self.snake.body[0]
        if head == self.food.pos:
            self.snake.score += 1
            self.snake.grow()
            self.food = Food(self.snake)
            
            
            
        #碰撞事件
        new_head_x,new_head_y = head
        if (head in self.snake.body[1:]
            or ((new_head_x >= SCREEN_W ) or new_head_x < 0)
            or ((new_head_y >= SCREEN_H ) or new_head_y < 0)):
            print("游戏结束")
            QMessageBox.warning(self,"游戏结束",f"得分{self.snake.score} 关闭窗口重启游戏")
            print("重启游戏")
            self.init_game()
            return
            
        # 触发界面刷新操作
        self.update()

    # 控制蛇的移动，要先获取键盘焦点  self.setFocusPolicy(Qt.StrongFocus)
    def keyPressEvent(self, event: QKeyEvent):
        self.snake.handle_event(event)

    def paintEvent(self, event: QPaintEvent):
        # return super().paintEngine()
        # 绘制画的内容
        # 创建画笔
        qp = QPainter(self)  # 父容器
        # 绘制背景
        qp.setBrush(COLOR_BLACK)  # R,G,B
        qp.drawRect(self.rect())
        # 绘制食物
        self.food.draw(qp)
        # 绘制蛇
        self.snake.draw(qp)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 创建窗口
    game = SnakeGame()
    game.show()
    # 让主程序阻塞运行
    sys.exit(app.exec())  # app.exec 让程序一直循环，sys.exit 把状态码传给系统
