# 1. https://school.programmers.co.kr/learn/courses/30/lessons/120891
'''
문제 설명
머쓱이는 친구들과 369게임을 하고 있습니다.
369게임은 1부터 숫자를 하나씩 대며 3, 6, 9가 들어가는 숫자는 
숫자 대신 3, 6, 9의 개수만큼 박수를 치는 게임입니다.
머쓱이가 말해야하는 숫자 order가 매개변수로 주어질 때, 
머쓱이가 쳐야할 박수 횟수를 return 하도록 solution 함수를 완성해보세요.

제한사항
1 ≤ order ≤ 1,000,000
입출력 예
order	result
3	1
29423	2
입출력 예 설명
입출력 예 #1

3은 3이 1개 있으므로 1을 출력합니다.
입출력 예 #2

29423은 3이 1개, 9가 1개 있으므로 2를 출력합니다.
'''
# 풀이 1
def solution(order):
    order_str = str(order)
    answer = 0
    for i in order_str:
        if int(i) % 3 == 0 and i != "0":
            answer +=1    
    return answer

print(solution(29423))

# 풀이 2 정규표현식으로 구하기
import re

def solution(order):
    p = re.compile('[3+6+9+]')
    return len(p.findall(str(order)))

print(solution(332345))

# 2. https://school.programmers.co.kr/learn/courses/30/lessons/12948
'''
문제 설명
프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.

제한 조건
phone_number는 길이 4 이상, 20이하인 문자열입니다.
입출력 예
phone_number	return
"01033334444"	"*******4444"
"027778888"	"*****8888"
'''