# https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    
    for command in commands:
        i,j,k = command[0],command[1],command[2]
        new_array = array[i-1:j]
        new_array.sort()
        answer.append(new_array[k-1])
        
    return answer