def solution(array,commands):
    answer=[]
    
    for command in commands:
        i,j,k=command                   #extraction i,j,k
        sliced_arr=array[i-1:j]
        sorted_arr=sorted(sliced_arr)
        answer.append(sorted_arr[k-1])
    
    return answer


print(solution([1,5,2,6,3,7,4],[[2,5,3],[4,4,1],[1,7,3]]))