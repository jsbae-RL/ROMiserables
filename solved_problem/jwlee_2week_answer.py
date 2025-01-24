def solution(x):
    y=len(str(x))                                             #to divide with units
    digit_sum=int((x//(10**y-1))+(x%(10**y-1)))               #//=return int  /=return floating point
    if x%digit_sum==0:                                        #if x is harshard
        return True
    else:
        return False

digit=int((input("enter the digit: ")))
print(solution(digit))                          #digit is argument






#not good code, but wanna modify