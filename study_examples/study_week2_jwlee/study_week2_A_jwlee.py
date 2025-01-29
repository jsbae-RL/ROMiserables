

def solution(x):
    sum_digit = 0       
    h_num = x
    while h_num > 0:
        sum_digit += h_num % 10     # 마지막 자릿수
        h_num //=10                 # 마지막 자릿수를 제거

    return x % sum_digit == 0       # 하샤드 수 여부 판단


print(solution(18))
print(solution(19))

