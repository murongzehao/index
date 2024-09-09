import random
import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtGui import QKeyEvent, QPaintEvent
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget


COLOR_BALCK = QColor(0,0,0)
COLOR_RED   = QColor(255,0,0)
COLOR_GREEN = QColor(0,255,0)
COLOR_BLUE  = QColor(0,0,255)

SCREEN_WIDTH,SCREEN_HEIGHT = 640,480
BLOCK_SIZE = 20
SCREEN_W = SCREEN_WIDTH // BLOCK_SIZE
SCREEN_H = SCREEN_HEIGHT // BLOCK_SIZE
DIR_UP     = (0,-1)
DIR_DOWN   = (0,1)
DIR_LEFT   = (-1,0)
DIR_RIGHT  = (1,0)

#创建窗口
class SnakeGame(QMainWindow):
    
    def __init__(self):
        super().__init__()
        #设置窗口图标
        self.setWindowIcon(QIcon("./img/icon.png"))
        #设置标题
        self.setWindowTitle("贪吃蛇小游戏")
        #固定框架大小(要有框架才能使用)
        # self.resize(640,480)
        self.setFixedSize(640,480)
        #创建画板 Frame
        self.frame = GameFrame(self)
        #将框架设置到当前窗口
        self.setCentralWidget(self.frame)
        
class Snake:
    
    def __init__(self):
        #  self.body = [[5,10],[4,10],[3,10]]
         self.body = [[5,10]]
         self.direction = DIR_RIGHT
         self.score = 0
         
         self.head_img = QImage("./img/head-red.png").scaled(BLOCK_SIZE,BLOCK_SIZE)
         
         
         #身体生长两格
         self.grow()
         self.grow()
         
         
         
    def move(self):
        #蛇动起来，蛇头在前进的方向复制一个，蛇尾删掉
        #1.获取蛇头的坐标
        head_x,head_y = self.body[0]
        dir_x,dir_y = self.direction
        #2.复制一个蛇头在原来的蛇头前面
        new_head = [head_x + dir_x,head_y + dir_y]
        self.body.insert(0,new_head)
        #3
        self.body.pop()
        
    
    def handle_event(self,a0:QKeyEvent):
          # return super().keyPressEvent(a0)   
        if a0.key() == Qt.Key_Up and self.direction != DIR_DOWN:
            self.direction = DIR_UP 
        elif a0.key() == Qt.Key_Down and self.direction != DIR_UP :
            self.direction = DIR_DOWN 
        elif a0.key() == Qt.Key_Left and self.direction != DIR_RIGHT:
            self.direction = DIR_LEFT 
        elif a0.key() == Qt.Key_Right and self.direction != DIR_LEFT:
            self.direction = DIR_RIGHT
            
    def draw(self,qp:QPainter):
        #绘制蛇身
         qp.setBrush(COLOR_GREEN)
         for x,y in self.body[1:]:
            qp.drawRect(x * BLOCK_SIZE,y * BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE)
            
        #绘制蛇头
         head_X,head_y = self.body[0]
         qp.drawImage(head_X * BLOCK_SIZE,head_y * BLOCK_SIZE ,self.head_img)
            
    def grow(self):
        #复制蛇身
        tail_x,tail_y = self.body[-1]
        #添加到尾部
        self.body.append([tail_x,tail_y])
        
class Food:
    
    def __init__(self,snake ) -> None:
        self.pos = self.generate_food(snake)
        
        
        #生成随机食物 
    def generate_food(self,snake : Snake):
        while True:
            pos = [random.randint(0,SCREEN_W - 1),random.randint(0,SCREEN_H - 1)]
            if pos not in snake.body:
                return pos
    def draw(self,qp:QPainter):
         #绘制食物
        qp.setBrush(COLOR_RED)
        qp.drawRect(self.pos[0] * BLOCK_SIZE,self.pos[1] * BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE)

#创建框架
class GameFrame(QFrame):
    
    def __init__(self, parent: QWidget):
        super().__init__(parent)
        #自动获取事件焦点
        self.setFocusPolicy(Qt.StrongFocus)
        self.init_game()
        #加self 变为类的属性
        self.bg_img = QImage("./img/bg.png").scaled(SCREEN_WIDTH,SCREEN_HEIGHT)
        
        
        
        #开启定时器，200ms刷新一次
        self.timer = QTimer(self) #绑定到父容器QMainwindow ,在父容器销毁时才自动销毁
        self.timer.timeout.connect(self.update_game)
        self.timer.start(200)
        
    def init_game(self):     
        self.snake = Snake()
        self.food = Food(self.snake)   

        
        
    #每一帧要做的事
    def update_game(self):
        # print("刷新界面:", time.time())

        self.snake.move()
        head = self.snake.body[0]
        #如果 吃掉了就加长，否则维持原样
        if head == self.food.pos:
            #吃到了食物，得分+1
            self.snake.score += 1
            #蛇身生长
            self.snake.grow()
            #食物重新生成
            self.food = Food(self.snake)
        
            
            
        #碰撞事件
        new_head_x,new_head_y = head
        if(head in self.snake.body[1:]
           or(new_head_x >= SCREEN_W or new_head_x < 0)
           or(new_head_y >= SCREEN_H or new_head_y < 0)):
            print("游戏结束")
            QMessageBox.warning(self,"游戏结束",f"得分:{self.snake.score},关闭窗口重启游戏")
            print("重启游戏")
            #重新初始化
            self.init_game()
            return
            
        
        #触发界面刷新
        self.update()
    
         
    def keyPressEvent(self, a0: QKeyEvent):
      self.snake.handle_event(a0)

        
    #绘制框架
    def paintEvent(self, event: QPaintEvent):
        # return super().paintEvent(a0)
        #创建画笔
        qp = QPainter(self)
        #绘制背景
        
        qp.drawImage(0,0,self.bg_img)
        #绘制食物
        self.food.draw(qp)
        #绘制蛇
        self.snake.draw(qp)
            
        



if __name__ == '__main__' :
    app = QApplication(sys.argv)
    #创建窗口
    game = SnakeGame()
    game.show()
    #让主程序阻塞，维持窗口
    sys.exit(app.exec_())