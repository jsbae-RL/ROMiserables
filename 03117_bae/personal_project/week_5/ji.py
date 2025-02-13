def solution(s):
    check = s.split(' ')
    for i in range(len(check)):
        check[i] = check[i].capitalize()
    print(check)
    return ' '.join(check)

print(solution("3people unFollowed me"))