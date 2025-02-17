# https://school.programmers.co.kr/learn/courses/30/lessons/250125

def solution(board, h, w):
    direction = [(-1,0),(1,0),(0,1),(0,-1)]
    count = 0
    n = len(board)
    
    
    for i,j in direction:
        
        neighbor_x = h + i
        neighbor_y = w + j
        
        if neighbor_x < 0 or neighbor_y < 0 or neighbor_x >= n or neighbor_y >= n:
            continue
        elif board[neighbor_x][neighbor_y] == board[h][w]:
            count +=1    
    
    return count

board =[["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]]
print(solution(board,1,1))

