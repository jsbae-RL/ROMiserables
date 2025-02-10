# 제한사항
# 1 ≤ order ≤ 1,000,000
# 입출력 예
# order	result
# 3	1
# 29423	2
# 입출력 예 설명
# 입출력 예 #1

# 3은 3이 1개 있으므로 1을 출력합니다.
# 입출력 예 #2

# 29423은 3이 1개, 9가 1개 있으므로 2를 출력합니다.
import re

max_order = 1000000
min_order = 1

def solution(s):
    answer = sum(map(lambda x : x in '369',str(s)))
    return answer

for i in range(1,40):

print(solution(29423))
print(solution(312993))