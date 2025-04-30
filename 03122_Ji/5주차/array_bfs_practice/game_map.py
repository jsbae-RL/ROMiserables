# https://school.programmers.co.kr/learn/courses/30/lessons/1844


# 처음에 푼 버전전
import numpy as np
from collections import deque

def ROR_game(map):
    visited = np.array(map)
    # 시작 위치
    st_x,st_y = 0,0
    # 상대 진영 위치
    n = visited.shape[0]
    m = visited.shape[1]
    
    q = deque()
    q.append((st_x,st_y))
    
    while True:
        if len(q) == 0:
            break
        
        # 로봇이 움직일 수 있는 방향
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # 현재 위치 -> 이미 이동했으므로 pop
        current_x, current_y = q.popleft()
        
        # 상하좌우 이동할 수 있는 좌표로 가봄
        for x,y in direction:
            if current_x == n-1 and current_y == m-1:
                break
            
            next_x = current_x + x
            next_y = current_y + y
            
            # 맵을 벗어나거나, 벽이면 갈 수 없음
            if next_x < 0 or next_y < 0 or next_x >= n or next_y >= m or\
                visited[next_x][next_y] == 0:
                continue
            if visited[next_x][next_y] == 1:
                q.append((next_x,next_y))
                visited[next_x][next_y] = visited[current_x][current_y] + 1
                
    if visited[n-1][m-1] == 1:
        return -1
    else:
        return visited[n-1][m-1]
    
    
                
map1 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
map2 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]] 
     
# print(ROR_game(map1))               


# 프로그래머스에 numpy 가 안되길래 뺀 버전 입니다.
import copy
from collections import deque

def ROR_game(map):
    visited = copy.deepcopy(map)
    
    # 시작 위치
    st_x,st_y = 0,0
    # 상대 진영 위치
    n = len(visited)
    m = len(visited[0])
    
    q = deque()
    q.append((st_x,st_y))
    
    while True:
        if len(q) == 0:
            break
        
        # 로봇이 움직일 수 있는 방향
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # 현재 위치 -> 이미 이동했으므로 pop
        current_x, current_y = q.popleft()
        
        # 상하좌우 이동할 수 있는 좌표로 가봄
        for x,y in direction:
            if current_x == n-1 and current_y == m-1:
                break
            
            next_x = current_x + x
            next_y = current_y + y
            
            # 맵을 벗어나거나, 벽이면 갈 수 없음
            if next_x < 0 or next_y < 0 or next_x >= n or next_y >= m or\
                visited[next_x][next_y] == 0:
                continue
            if visited[next_x][next_y] == 1:
                q.append((next_x,next_y))
                visited[next_x][next_y] = visited[current_x][current_y] + 1
                
    if visited[n-1][m-1] == 1:
        return -1
    else:
        return visited[n-1][m-1]
    
map1 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
map2 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]] 
     
print(ROR_game(map1)) 

                
            
            
            
    
    
    

