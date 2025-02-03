def solution(order):
    num_list = list(str(order))
    answer = 0
    for num in num_list:
        if num in '369':
            answer += 1
    print(answer)
    return answer