import turtle
from logistics import map_Directions

class draw_path():
    def __init__(self,logistics_map):

        self.logistics_map = logistics_map
        self.row,self.columns = logistics_map.shape
        self.draw_map()
        self.goto_zreo()


    def draw_map(self):
        turtle.speed(0)
        turtle.hideturtle()
    
        for i in range(self.row):
            for j in range(self.columns):
                x,y = j*20 -100, 100- i*20  #그림은 +x -y인데 값은 x,y여서 변환

                turtle.penup()
                turtle.goto(x,y)
                turtle.pendown()

                if self.logistics_map[i, j] == 2:  # 시작 위치
                    turtle.color("blue")
                elif self.logistics_map[i, j] >= 3:  # 제품 위치
                    turtle.color("white")
                else:
                    turtle.color("black")
                turtle.begin_fill()
                for _ in range(4):
                    turtle.forward(20)
                    turtle.right(90)
                turtle.end_fill()
        turtle.color("black")

    def draw_move_path(self,color, target_number=None,start=2):
        find_move_path = map_Directions(self.logistics_map,target_number,start)
        move_path = find_move_path.bfs_map()
        turtle.speed(2)
        turtle.pensize(2)
        turtle.color(color)
        for (i, j) in move_path:
            x, y = j * 20 - 90, 90 - i * 20  # 좌표 변환
            turtle.goto(x, y)
        self.goto_zreo()

    def goto_zreo(self):
        turtle.setup(300, 300)
        turtle.penup()
        turtle.goto(-90, 90)  # 시작 위치 설정
        turtle.pendown()