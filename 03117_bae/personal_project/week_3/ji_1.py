
def solution(s):
    number_dict = {
    'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
    'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
}

    answer = ''
    change = ''
    count = 0

    while count < len(s):
        change += s[count]

        if change in number_dict:  # 영어 숫자 변환
            answer += number_dict[change]
            change = ''
        elif s[count].isdigit():  # 숫자 그대로 추가
            answer += s[count]
            change = ''  # change 초기화

        count += 1

    return int(answer)