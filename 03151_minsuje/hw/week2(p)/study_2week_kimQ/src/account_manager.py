from src import file_reader

class AccountManager:
    def __init__(self):
        self.accounts = self.load_accounts()

    def load_accounts(self):
        """계정 데이터를 파일에서 로드"""
        return file_reader.read_accounts()

    def save_accounts(self):
        """현재 계정 데이터를 파일에 저장"""
        file_reader.write_accounts(self.accounts)

    # return된 값은 massgebox를 통해 화면에 표시됨.
    def create_account(self, username, password):
        """새 계정 생성"""
        if username in self.accounts:   #가지고 있는 계정에 입력받은 이름이 있는지 확인 있으면 이미 존재하는 아이디
            return "이미 존재하는 아이디입니다."
        if not username.isalnum():  #입력받은값이 숫자와 영어가 아닐경우
            return "아이디는 숫자와 영어문자만 입력 가능합니다."
        if not any(char.isdigit() for char in password):    #입력받은 비밀번호가 숫자가 포함되지 않았을때
            return "비밀번호에 숫자가 포함되어야 합니다."
        if not any(char.isalpha() for char in password):    #입력 받은 비밀번호가 영어 문자가 포함 되어 있지 않을때
            return "비밀번호에 영어문자가 포함되어야 합니다."
        #계정을 저장하여 file_reader를 통해 txt에 저장.
        self.accounts[username] = {'password': password, 'failed_attempts': 0}
        self.save_accounts()
        self.accounts = self.load_accounts()
        return "계정이 생성되었습니다."

    # return된 값은 massgebox를 통해 화면에 표시됨.
    def login(self, username, password):
        self.accounts = self.load_accounts()
        """로그인 처리"""
        if username not in self.accounts:   #입력 받은 값이 계정에 존재하지 않는다면
            return "아이디가 존재하지 않습니다."
        if self.accounts[username]['failed_attempts'] >= 3: #입력 받은 계정의 'failed_attempts'의 겂이 3 이상이면(틀린횟수 3회이상)
            return "계정이 잠겼습니다."
        if self.accounts[username]['password'] == password: # 비밀번호가 일치하면
            self.accounts[username]['failed_attempts'] = 0  # 비밀번호 틀린횟수 초기화
            self.save_accounts()    #초기화된 틀린횟수 저장
            return "로그인에 성공했습니다."
        else:                                               #비밀번호가 틀렸을때
            self.accounts[username]['failed_attempts'] += 1 #비밀번호 틀린 횟수 1추가
            self.save_accounts()                            #틀린 횟수 저장.
            return "비밀번호가 잘못되었습니다."