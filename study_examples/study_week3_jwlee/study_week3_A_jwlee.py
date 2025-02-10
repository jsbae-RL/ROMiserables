# 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 
# 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

# 제한 조건
# 행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.
# 입출력 예
# arr1 = [[[1, 2], [2, 3]], [[1], [2]]]	    
# arr2 = [[[3, 4], [5, 6]], [[3], [4]]]
# return [[[4, 6], [7, 9]], [[4], [6]]]


# # 풀이

# 1. 2차원 배열

def solution(arr1, arr2):
    result = []
    for row in range(len(arr1)):            # 행 반복
        new_row = []
        for col in range(len(arr1[0])):     # 열 반복
            new_row.append(arr1[row][col] + arr2[row][col])      # 한 행 완성, result에 추가
        result.append(new_row)
    return result

arr1 = [[1, 2], [2, 3]]
arr2 = [[3, 4], [5, 6]]

print(solution(arr1, arr2))

print('----')

import numpy as np

def solution(arr1, arr2):
    
    result = np.add(arr1, arr2)
    return list(result) 

arr1 = [[1, 2], [2, 3]]
arr2 = [[3, 4], [5, 6]]

print(solution(arr1, arr2))

print('----')

# 2. lambda 와 map 함수를 사용(gpt 활용)
def solution(arr1, arr2):
    # map과 lambda를 사용해 2차원 배열의 요소를 더함
    return list(map(lambda row1, row2: list(map(lambda x, y: x + y, row1, row2)), arr1, arr2))

# 테스트
arr1 = [[1, 2], [2, 3]]
arr2 = [[3, 4], [5, 6]]

print(solution(arr1, arr2))  # 출력: [[4, 6], [7, 9]]


print('----')

#      3. 3차원배열 (구현 실패)

# import numpy as np

# def solution(arr1, arr2):
    
#     result = np.add(arr1, arr2)
#     return list(result) 


# arr1 = [[[1, 2], [2, 3]], [[1], [2]]]
# arr2 = [[[3, 4], [5, 6]], [[3], [4]]]

# print(solution(arr1, arr2))


# def solution(arr1, arr2):
#     result = []
#     for i in range(len(arr1)):      # 3차원 배열의 층 반복
#         two_d=[]                    # 2차원 배열 합
#         for row in range(len(arr1[i])):     # 행 반복
#             row_list = []
#             for col in range(len(arr1[i][row])):    # 열 반복
#                 row_list.append(arr1[i][row][col] + arr2[i][row][col])      # 한 행 완성, result에 추가
#             two_d.append(row_list)
#         result.append(row_list)
#     return result

# arr1 = [[[1, 2], [2, 3]], [[1], [2]]]	    
# arr2 = [[[3, 4], [5, 6]], [[3], [4]]]

# print(solution(arr1, arr2))  