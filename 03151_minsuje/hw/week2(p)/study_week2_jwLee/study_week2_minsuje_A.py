def is_harshad_num(x):
    if not 1<=x<=10000: #범위 확인
        return
    sum_digits = 0      #자리수 합을 구할 변수 초기화
    strxs = str(x)      #x를 문자화 해서 문자열 각각을 int로 변환 하고 자리수의 합을 구함.
    for strx in strxs:
        sum_digits+= strx
    return x%sum_digits==0  #x를 자리수의 합으로 나누어 나머지가 0이면 하샤드수수

def solution(x):
    answer = is_harshad_num(x)
    return answer