import os

# 파일 경로 설정
FILE_PATH = "C:/ROKEY/ROMiserables/ROMiserables/03151_minsuje/hw/week2(py)/study_2week_kimQ/src/account.txt"
#읽기
def read_accounts():
    '''txt파일 내용 읽기'''
    accounts = {}
    with open(FILE_PATH, 'r') as f:
        for line in f:                      # 한줄씩 확인함.
            parts = line.strip().split(',') #,로 분리하며 띄어쓰기 없긴한데 없앴음.
            if len(parts) == 3:             #읽은 데이터가 3개가 아니면 잘못된 데이터 읽기 혹은 잘못된 데이터가 저장되어 있음.(현재 비밀번호에,가 들어가는데 들어가면 ㅇ 4개나옴)
                accounts[parts[0]] = {                  #계정 아이디에
                    'password': parts[1],               #비밀번호
                    'failed_attempts': int(parts[2])    #틀린횟수
                }
    return accounts                                     #읽어온 계정 반환환
#쓰기
def write_accounts(accounts):
    '''txt파일 내용 쓰기 - 이미 있는 내용은 수정되고 없는 내용은 새로 써짐
    한번에 다쓰는 식으로 했음 해당 부분만 수정하는게 아니라 통째로 수정함.
    차후 같은 내용의 이름이 있으면 수정 없으면 추가 하는식으로 수정하는것도 좋을지도
    '''
    with open(FILE_PATH, 'w') as f:
        for username, data in accounts.items():                                     #입력된 데이터 분리
            f.write(f"{username},{data['password']},{data['failed_attempts']}\n")   #데이터 가공및 저장