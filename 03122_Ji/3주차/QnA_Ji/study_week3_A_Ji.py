# 1
import re
numbers=['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def solution(s):
  for idx, num in enumerate(numbers): # numbers 리스트와 인덱스를 같이 처리(0,1,2,3...)
    p = re.compile(num)               # numbers 요소를 비교로 설정정
    if p.search(s):                   # 문자열 처음부터 끝까지 검색해서 존재하면면
      s= s.replace(num,str(idx))      # 문자열에서 numbers요소 부분을을 그 인덱스를 문자열화 한것으로 대체
  return int(s)                       # '숫자'로 대체한한 문자열을 정수형으로 변환하여 반환환
    
s = 'one4seveneight'
print(solution(s))


# 2.
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

print(solution('bbbba'))


# 3
def solution(s):
  nums = s.split()                            # 공백을 기준으로 나눠 리스트로 저장장
  nums = list(map(lambda x: int(x), nums))    # 리스트 내부 문자열숫자를 정수로 변환환
  max_num = max(nums)                         
  min_num = min(nums)
  result_list = [min_num, max_num]            # 최소값, 최대값을 차례대로 결과 리스트에 저장
  result_list = list(map(lambda x: str(x), result_list))  # 내부 요소를 문자열숫자로 변환
  result = " ".join(result_list)              # 공백을 기준으로 하나의 문자열로 저장
  return result

s = input('숫자를 입력하세요:')
print(solution(s))
