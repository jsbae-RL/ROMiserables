
import numpy as np

def solution(n, left, right):
    # n x n 2차원 배열 생성, 값 채우기
    matrix = np.fromfunction(lambda i, j : np.maximum(i, j) + 1, (n, n), dtype=int)  # np.fromfunction( (인덱스x,y) , shape, dtype=정수)
    
    arr = matrix.flatten()      # 2차원 배열을 1차원 배열로 변환
    return arr[left:right+1].tolist()  


print(solution(3, 2, 5))  # [3,2,2,3]
print(solution(4, 7, 14)) # [4,3,3,3,4,4,4,4]
