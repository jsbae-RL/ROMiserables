# Q1. 로그인 시에 아이디를 검사하는 함수 check()를 작성해서 테스트하라. 
# check가 한 번 호출 될 때마다 비밀번호를 질문하고 일치여부를 확인한다.
# 비밀번호는 숫자 1234로 고정되어있다고 가정한다.
# check가 3번 이상 호출되고 아이디가 일치하지 않으면 check()는 "Account has exceed allowed number of login attempts."메시지를 출력한다.

def check():
    password = input('password: ')
    if password == '1234':
        return True
    else:
        return False
    
for i in range(3):                    # check 호출 3번 반복
    result = check()
    if result:                        # result == True
        print('로그인 성공')
        break
    elif i==2:                        # result == False 고 i == 2(3번째 입력일 때)
        print('Account has exceed allowed number of login attempts.')
    
        
        
'''
Result

password: 1000
password: 1001
password: 1002
Account has exceed allowed number of login attempts.
'''