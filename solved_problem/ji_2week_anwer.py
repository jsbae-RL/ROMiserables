def solution(s):                                                   
    if len(s)==4 or len(s)==6:                     #count string length             
            if s.isdigit()==True:                  # is digit? T/F  
                return True
            else:
                return False
    else:                                          #string length is not 4 or 6
        return False
            

print(solution("a234"))
print(solution("1234"))