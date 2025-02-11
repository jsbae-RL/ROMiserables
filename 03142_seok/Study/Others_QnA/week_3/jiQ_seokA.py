#1
'''
0	zero
1	one
2	two
3	three
4	four
5	five
6	six
7	seven
8	eight
9	nine

# 아이디어 1
1. 알파벳을 발견하면 이를 push 하는 스택, converter 리스트가 필요하다.
2. 단어의 첫글자와 마지막 글자가 아래 예시에 따라 일치하면 숫자로 변환하는 코드
3. 예시 : ['z', 'e', 'r', 'o'] 일시 첫글자 'z'와 마지막 'o'만을 확인하면 'zero'임을 알 수 있다.
4. 숫자만을 기록하는 number 리스트에 number.append(0)를 하고, 
5. converter.clear()로로 다시 converter 리스트를 빈 상태로 만든다.
6. 이를 반복하면 number 리스트에 기존의 숫자와 변환된 숫자를 전부 기록할 수 있다.

# 문제점 : 영문 오타시 프로그램이 고장이 난다. 그냥 딕셔너리로 하는게 맞는 것 같다. (폐기)
'''
num_card = input("넘버를 입력하세요: ")
number = []                         # 숫자만을 기록하는 number 리스트
converter = []                      # 영어를 숫자로 변환하는 converter 리스트 

for char in num_card:               # 넘버카드의 한글자씩 가져와서
    try:                            # int로 변환을 시도 하고
        int_value = int(char)
        number.append(int_value)    # 성공한다면 number 리스트에 바로 넣고
        converter.clear()
    except ValueError:              # 실패한다면 문자로 간주한다.
        converter.append(char)
        if converter[0] == "z":     # zero 탐색
            if converter[-1] == "o":
                number.append(0)    # number 리스트에 0을 삽입하고
                converter.clear()   # converter 리스트를 리셋 한다.

        elif converter[0] == "o":   # zero가 없다면 one, one이 없다면 two ~ nine 까지 찾아낸다.
            if converter[-1] == "e":
                number.append(1)
                converter.clear()

        elif converter[0] == "t":
            if converter[-1] == "o":
                number.append(2)
                converter.clear()
            elif converter[-1] == "e":
                number.append(3)
                converter.clear()

        elif converter[0] == "f":
            if converter[-1] == "r":
                number.append(4)
                converter.clear()
            elif converter[-1] == "e":
                number.append(5)
                converter.clear()

        elif converter[0] == "s":
            if converter[-1] == "x":
                number.append(6)
                converter.clear()
            elif converter[-1] == "n":
                number.append(7)
                converter.clear()

        elif converter[0] == "e":
            if converter[-1] == "t":
                number.append(8)
                converter.clear()

        elif converter[0] == "n":
            if converter[-1] == "e":
                number.append(9)
                converter.clear()
for n in number:
    print(n, end="")

'''
# 아이디어 2 (문자열과 딕셔너리 활용)

num_card = input("넘버를 입력하세요: ")
number = []     # 숫자 리스트
converter = ""  # 변환 문자열

# 영어 단어를 숫자로 변환하는 딕셔너리
word_to_digit = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
}

for char in num_card:
    if char.isdigit():  # 숫자인 경우
        number.append(int(char))
        converter = ""  # 기존 변환 대기 문자열 초기화
    else:  # 문자일 경우
        converter += char  # 문자 누적

        # 현재 converter 값이 단어 딕셔너리에 있는지 확인
        if converter in word_to_digit:
            number.append(word_to_digit[converter])  # 변환 후 리스트에 추가
            converter = ""  # 변환이 완료되었으므로 초기화

for n in number:
    print(n, end="")

'''

#2
