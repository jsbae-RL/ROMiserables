def solution(num):
    for i in range(500):
        if num==1:
            return i                            #if num is 1, return count of current cycle i
        num=num//2 if num%2==0 else num*3+1      #if num is even, divide with 2  if num is odd, multi 3 and add 1
    return -1                                   #again 500 times, num!=1->return -1




#삼항연산자
# value1 if condition else value2
