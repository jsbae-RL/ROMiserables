def solution(arr):
    result=[]                       #new list(to return)
    for i in arr:                   #search i duplication
        if i not in result:         
            result.append(i)
    return result


arr1=[1,1,3,3,0,1,1]
arr2=[4,4,4,3,3]
print(solution(arr1))
print(solution(arr2))