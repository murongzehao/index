import random
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import *
from snake import *

class Food:
    
    def __init__(self,snake) -> None:
        self.pos = self.generate_food(snake)
    
    
    def generate_food(self,snake : Snake):       
        while True:           
            pos = (random.randint(0,SCREEN_W - 1),random.randint(0,SCREEN_H - 1))
            if pos not in snake.body:
                return pos    
    
    def draw(self,qp:QPainter):
        qp.setBrush(COLOR_RED)  # Red, Green, Blue
        qp.drawRect(self.pos[0] * BLOCK_SIZE, self.pos[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
        