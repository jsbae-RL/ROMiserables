# 2. 문제 설명
'''
문자열 s가 입력되었을 때 다음 규칙을 따라서 이 문자열을 여러 문자열로 분해하려고 합니다.

- 먼저 첫 글자를 읽습니다. 이 글자를 x라고 합시다.
- 이제 이 문자열을 왼쪽에서 오른쪽으로 읽어나가면서, x와 x가 아닌 다른 글자들이 나온 횟수를 각각 셉니다.
  처음으로 두 횟수가 같아지는 순간 멈추고, 지금까지 읽은 문자열을 분리합니다.
- s에서 분리한 문자열을 빼고 남은 부분에 대해서 이 과정을 반복합니다. 남은 부분이 없다면 종료합니다.
- 만약 두 횟수가 다른 상태에서 더 이상 읽을 글자가 없다면, 역시 지금까지 읽은 문자열을 분리하고, 종료합니다.

문자열 s가 매개변수로 주어질 때, 위 과정과 같이 문자열들로 분해하고, 분해한 문자열의 개수를 return 하는 함수 solution을 완성하세요.

제한사항
1 ≤ s의 길이 ≤ 10,000
s는 영어 소문자로만 이루어져 있습니다.

입출력 예
    s	        result
"banana"	      3
"abracadabra"	  6
"aaabbaccccabba"  3

입출력 예 설명
입출력 예 #1
s="banana"인 경우 ba - na - na와 같이 분해됩니다.

입출력 예 #2
s="abracadabra"인 경우 ab - ra - ca - da - br - a와 같이 분해됩니다.

입출력 예 #3
s="aaabbaccccabba"인 경우 aaabbacc - ccab - ba와 같이 분해됩니다.
'''
from collections import deque

def solution(s):
  dq = deque(s)
  count = 0                     # 몇 개의 부분으로 분해되었는지 저장하는 변수수
  
  while dq:
    if len(dq) == 1:            # 문자열이 처음부터 한글자거나, 한글자만 남았을 때
      count += 1                
      
    x = dq.popleft()            # 첫번째 요소를 x에 저장(덱에서 삭제제)
    count_x = 1                 # x 개수를 저장할 변수 초기화 (처음 하나가 있으니 1)
    count_a = 0                 # x와 다른 문자 개수를 저장할 변수 초기화화
    
    while dq:
      if x == dq[0]:            # 그 다음요소가 x와 같으면면
        count_x += 1            # x 개수 +1
        dq.popleft()            # 그리고 검사한 요소는 삭제제
      else:
        count_a += 1            # 그 다음요소가 x와 다르면면 a에 +1
        dq.popleft()            # 그리고 검사한 요소 삭제
      
      if count_x == count_a:    # 검사 후 x와 다른문자의 개수가 같으면
        count += 1              # count 변수에 +1 하고 내부 반복문 탈출출
        break
      elif len(dq) == 0:        # 만약 개수가 다른데 문자열을 다 확인했다면
        count += 1              # count 변수에 +1 하여 한덩어리임을 저장장
  return count  

print(solution("banana"))
print(solution("abracadabra"))
print(solution("aaabbaccccabba"))
from collections import deque
dq = deque([1, 2, 3])
dq.appendleft(0)
print(dq)
