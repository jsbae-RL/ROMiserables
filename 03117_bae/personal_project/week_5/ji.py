def solution(s):
    check = s.split(' ') # 공백을 하나만 준다면, 공백이 여러개도 하나만 제외하고 분리
    # print(check)
    # ['3people', '', '', '', '', '', 'unFollowed'] 결과 = 공백이 한칸만 제외하고 5칸은 하나씩 리스트로
    for i in range(len(check)):
        # title() # 문자 단어의 앞글자가 숫자면, 그 숫자 다음 문자를 대문자로 수정
        check[i] = check[i].capitalize()
        # title 결과 = 3People      Unfollowed
        # capi() 결과 = 3people      Unfollowed
    # print(check)
    return ' '.join(check) # split(' ' )으로 없애줬던 공백을 join으로 추가하면서 return
    # 3people123456Unfollowed
print(solution("3people      unFollowed")) # 3people + 띄어쓰기 6칸 + un

# title