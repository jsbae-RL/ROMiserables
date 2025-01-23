# Q1. 로그인 시에 아이디를 검사하는 함수 check()를 작성해서 테스트하라. 
# check가 한 번 호출 될 때마다 비밀번호를 질문하고 일치여부를 확인한다.
# 비밀번호는 숫자 1234로 고정되어있다고 가정한다.
# check가 3번 이상 호출되고 아이디가 일치하지 않으면 check()는 "Account has exceed allowed number of login attempts."메시지를 출력한다.

'''
Result

password: 1000
password: 1001
password: 1002
Account has exceed allowed number of login attempts.
'''

password = 1234
count = 0

def check():
    global count
    while count<4:
        p = int(input('비밀번호를 입력해주세요 : '))
        if p == password:
            print('비밀번호가 일치합니다.')
            break
        else:
            count += 1
            if count ==3:
                print('Account has exceed allowed number of login attempts.')
                break

check()



    


