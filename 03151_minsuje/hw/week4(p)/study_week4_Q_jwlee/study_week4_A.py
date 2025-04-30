def solution(arry):
    answer = [arry[0]]
    for index in range(1,len(arry),1):
        if arry[index]!=arry[index-1]:
            answer.append(arry[index])
    return answer
arry = [1,1,3,3,0,1,1]
arry2 = [4,4,4,3,3]
print(solution(arry))
print(solution(arry2))