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

correct_pw=1234
count=0
def check():
    """
    Check the password
    """
    global count
    while True:
        enter_pw=int(input("enter the password(within 3 times): "))
        if correct_pw==enter_pw:
            print("Login successful.")
            break
        elif correct_pw!=enter_pw:
            count+=1
            if count==3:
                print("Account has exceed allowed number of login attempts.")
                break

check()
