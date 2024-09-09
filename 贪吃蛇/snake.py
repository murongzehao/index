import random
import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtGui import QKeyEvent, QPaintEvent
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget

DIR_UP = (0, -1)
DIR_DOWM = (0, 1)
DIR_LEFT = (-1, 0)
DIR_RIGHT = (1, 0)

COLOR_BLACK = QColor(0, 0, 0)
COLOR_RED = QColor(255, 0, 0)
COLOR_GREEN = QColor(0, 255, 0)

SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
BLOCK_SIZE = 20  # 块大小
SCREEN_W = SCREEN_WIDTH // BLOCK_SIZE  # 32
SCREEN_H = SCREEN_HEIGHT // BLOCK_SIZE  # 24

class Snake:
    
    def __init__(self) -> None:
                # 初始化蛇的位置，大小
        # self.body = [[5, 10], [4, 10], [3, 10]]
        self.body = [[5,10]]
        # 初始化蛇前进的方向
        self.direction = DIR_RIGHT
        # 得分
        self.score = 0
        
        #复制两截身体
        self.grow()
        self.grow()
        
    def move(self):
         # 1.获取蛇头坐标
        head_x, head_y = self.body[0]
        dir_x, dir_y = self.direction
        # 2.根据前进方向添加蛇头
        new_head = (head_x + dir_x, head_y + dir_y)
        self.body.insert(0, new_head)       
        # 3. 删除蛇尾 （没吃到食物时，需要删除）
        self.body.pop()
        
    def handle_event(self,event:QKeyEvent):
        # print(event.key())  # 上下左右
        if event.key() == Qt.Key_Up and self.direction != DIR_DOWM:
            # print("向上")
            self.direction = DIR_UP
        if event.key() == Qt.Key_Down and self.direction != DIR_UP:
            # print("向上")
            self.direction = DIR_DOWM
        if event.key() == Qt.Key_Left and self.direction != DIR_RIGHT:
            # print("向上")
            self.direction = DIR_LEFT
        if event.key() == Qt.Key_Right and self.direction != DIR_LEFT:
            # print("向上")
            self.direction = DIR_RIGHT
            
    def draw(self,qp:QPainter):
        qp.setBrush(COLOR_GREEN)
        for x, y in self.body:
            qp.drawRect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            
    def grow(self):
        #复制蛇尾
        tail_x,tail_y = self.body[-1]
        #添加进蛇尾
        self.body.append([tail_x,tail_y])