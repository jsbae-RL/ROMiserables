def solution(numbers, target):
    answer = 0                                  
    n=len(numbers)
    def dfs(index1,result):                         #dfs function(now search digit's index,now sum)
        nonlocal answer                             #nonlocal==various answer can change in dfs function
        if index1==n:                               #when use all digits in list   ex)numbers=[1,1,1,1,1]==>index1=5
            if result==target:                      
                answer+=1
            return                                  #function off
        else:
            dfs(index1+1,result+numbers[index1])    #add now number    index1+1==>move next num, and result+numbers[index1]
            dfs(index1+1,result-numbers[index1])    #sub now number    index1+1==>move next num, and result-numbers[index1]
    dfs(0,0)                                        #start search  index==0 result==0
    return answer