# 1
def solution(order):
    num_list = list(str(order))
    answer = 0
    for num in num_list:
        if num in '369':
            answer += 1
    print(answer)
    return answer

# 2
def solution(phone_number):
    phone_number = list(phone_number)
    for idx in range(len(phone_number[:-4])):
        phone_number[idx] = '*'
    answer = ''.join(phone_number)
    return answer