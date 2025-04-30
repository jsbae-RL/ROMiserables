# 1
def solution(order):
    num_list = str(order)
    answer = 0
    for num in num_list:
        if num in '369':
            answer += 1
    print(answer)
    return answer

# 2  sub 으로 하는 방법
def solution(phone_number):
    phone_number = list(phone_number)
    for idx in range(len(phone_number[:-4])):
        phone_number[idx] = '*'
    answer = ''.join(phone_number)
    return answer

print(solution('01064289769'))