
# 3. 문제 설명
'''
문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다.
str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수, solution을 완성하세요.
예를들어 s가 "1 2 3 4"라면 "1 4"를 리턴하고, "-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.

제한 조건
s에는 둘 이상의 정수가 공백으로 구분되어 있습니다.

입출력 예
s	            return
"1 2 3 4"	    "1 4"
"-1 -2 -3 -4"	"-4 -1"
"-1 -1"	        "-1 -1"
'''
def solution(s):
  nums = s.split()                            # 공백을 기준으로 나눠 리스트로 저장장
  nums = list(map(lambda x: int(x), nums))    # 리스트 내부 문자열숫자를 정수로 변환환
  max_num = max(nums)                         
  min_num = min(nums)
  result_list = [min_num, max_num]            # 최소값, 최대값을 차례대로 결과 리스트에 저장
  result_list = list(map(lambda x: str(x), result_list))  # 내부 요소를 문자열숫자로 변환
  result = " ".join(result_list)              # 공백을 기준으로 하나의 문자열로 저장
  return result

print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 1"))