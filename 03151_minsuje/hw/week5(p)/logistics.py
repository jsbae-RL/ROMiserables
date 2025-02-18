import pandas as pd
import numpy as np
from collections import deque

class map_Directions():
    def __init__(self,logistics_map, target_number=None, start_number=2):
        self.start_num = start_number
        self.target_num = target_number
        self.logistics_map = logistics_map
        self.row,self.columns = logistics_map.shape       #맵의 크기를 튜플 값으로 받음 shape는 np의 객체 속성이라 따로 함수가 아님... 튜플로 크기 반환해줌
        self.visit_df = pd.DataFrame(False, index=range(self.row),columns=range(self.columns))
        self.target = self.find_pos(target_number)
        self.start = self.find_pos(start_number)
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.visit_df.iloc[self.start] = True    #시작점 설정

    def find_pos(self, number):
        for i in range(self.row):
            for j in range(self.columns):
                if self.logistics_map[i,j] == number:
                    return (i,j)

    def bfs_map(self):
        queue = deque([((self.start), [self.start])]) #현재 위치, 경로 초기화

        while queue:
            (x,y), path = queue.popleft()

            if(x,y) == self.target:
                return path
            
            for dx, dy in self.directions:
                new_x, new_y =x+dx, y+dy
                
                #맵크기를 벗어 나지 않고
                #맵에 길과 시작지점, 타겟지점에 있는지 확인
                #그리고 이미 방문 한 곳이 아니면
                if 0<= new_x <self.row and 0<=new_y <self.columns \
                    and self.logistics_map[new_x,new_y]in [0, self.start_num, self.target_num]\
                    and not self.visit_df.iloc[new_x, new_y]:
                        self.visit_df.iloc[new_x, new_y] = True   #방문지정
                        queue.append(((new_x, new_y), path + [(new_x, new_y)]))
        return None #경로 없음.