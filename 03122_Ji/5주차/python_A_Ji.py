# 저는 다른 부분은 잘 모르겠어서 맵이 주어졌을 때 turtle을 이용해 맵을 그리고
# 시작 위치와 장애물을 표시하는 모듈만드는 부분을 구현해봤습니다!

import turtle
import pandas as pd
import numpy as np

# start position = (-300,200)

class Draw_map:
    mag = 50
    
    def __init__(self,map):
        self.map= map
        turtle.setup(800,500)
        self.t = turtle.Turtle()
        self.t.speed(0)
        
    def draw_map(self):
        self.map_size = list(self.map.shape)
        self.edge_x = self.map_size[0]-1
        self.edge_y = self.map_size[1]-1
        
        self.t.penup()
        self.t.goto(-300,200)
        self.t.pendown()
        
        self.t.goto(-300 + self.edge_y * Draw_map.mag, 200)
        self.t.goto(-300 + self.edge_y * Draw_map.mag, 200 - self.edge_x * Draw_map.mag)
        self.t.goto(-300 , 200 - self.edge_x * Draw_map.mag)
        self.t.goto(-300,200)
        
        for i in range(1,self.map_size[1]):
            self.t.penup()
            self.t.goto(-300 + i * Draw_map.mag, 200)
            self.t.pendown()
            self.t.setheading(-90)
            self.t.forward(self.edge_x*Draw_map.mag)
            
        
        for i in range(1,self.map_size[0]):
            self.t.penup()
            self.t.goto(-300, 200 - i * Draw_map.mag)
            self.t.pendown()
            self.t.setheading(0)
            self.t.forward(self.edge_y*Draw_map.mag)
            
        self.t.hideturtle()
            
            
    def draw_obstacle(self):
        self.rows,self.cols = np.where(self.map>2)
        self.obstacle = list(zip(self.rows,self.cols))
        
        self.t.penup()
        self.t.goto(-300,200)
        self.t.dot(10,'green')
        
        for coordi in self.obstacle:
            self.t.penup()
            self.t.goto(-300 + coordi[1]* Draw_map.mag, 200 - coordi[0] * Draw_map.mag)
            self.t.pendown()
            self.t.dot(10,'red')
            
        self.t.hideturtle()
    
    def exit(self):
        turtle.exitonclick()
        
    
if __name__ == '__main__':
    map = np.array([
    [  2,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [  0,  3,  0,  4,  0,  5,  0,  6,  0,  0],
    [  0,  0,  0,  0,  7,  0,  0,  8,  0,  0],
    [  0,  9,  0, 10,  0, 11,  0, 12,  0,  0],
    [  0,  0,  0,  0, 13,  0,  0,  0, 14,  0],
    [  0, 15,  0, 16,  0, 17,  0, 18,  0,  0],
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
    ])


    map_drawer = Draw_map(map)

    map_drawer.draw_map()
    map_drawer.draw_obstacle()
    map_drawer.exit()
