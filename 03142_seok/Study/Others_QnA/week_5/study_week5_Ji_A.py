# 풀이 1번(간단한 풀이가 생각나면 더 추가하겠습니다!)
import re
ref = 'for   the last week'
ref2 = "3people unFollowed me"

def solution(s):
    p = re.compile('\w+')                       # 단어 검출 패턴턴
    sp = re.compile('\s+')                      # 공백 검출 패턴
    m = p.findall(s)                            # 문자열에서 단어 검출해서 리스트에 저장
    s = sp.findall(s)                           # 문자열에서 공백 검출해서 리스트에 저장

    answer = ''                                 # 답 저장할 빈 문자열 생성
    for i, word in enumerate(m):                # 단어 리스트의 단어와 인덱스를 차례로 가져옴
        if word[0].isalpha() and word[0].islower():     # 가져온 단어의 첫글자가 알파벳인데 소문자면
            answer += word[0].upper()                   # 대문자로 변환하여 답 문자열에 더함
        else:                                   # 숫자거나나 대문자면 그대로 답 문자열에 더함
            answer+= word[0]
        
        for char in word[1:]:                   # 단어의 두번째 글자부터 끝까지 하나하나 탐색
            if char.isalpha() and char.isupper():   # 글자 중 알파벳이고, 대문자인 것이 있으면
                answer+=char.lower()                # 소문자로 변환하여 답 문자열에 더함
            else:
                answer+=char                        # 숫자거나 소문자면 그대로 더함
        if i < len(s):                              # 원래 주어진 문자열 s와 같아 지도록
            answer += s[i]                          # 검출한 공백을 답 문자열에 더함
    # for   the last week 가 들어왔으면
    # 1. m = [for,the,last,week] 와 s = [   , , ] 두 리스트가 있고
    # 2. m 에서 for 문 돌려 첫번째로 for을 가져오면
    #   2-1. f -> 소문자이므로 F로 변환하여 answer += 'f' 현재answer: 'f'
    #   2-2. o,r 은 둘다 소문자 이므로 그대로 더함 현재 answer: 'for'
    #   2-3. s[0]에 들어있는 공백을 가져옴 -> 원래 문자열과 동일한 구성이 되도록함 현재 answer: 'for   '
    # 이를 반복해서 answer에 계속 저장함 (answer에 문자가 계속 쌓임)
    
    return answer