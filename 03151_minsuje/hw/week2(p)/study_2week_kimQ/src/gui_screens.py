import tkinter as tk
from tkinter import messagebox
from src.account_manager import AccountManager

class GUIScreens:
    def __init__(self, root):
        '''초기화'''
        self.root = root
        self.account_manager = AccountManager()

        # 화면 프레임 생성
        self.main_menu_frame = tk.Frame(root)
        self.login_frame = tk.Frame(root)
        self.create_account_frame = tk.Frame(root)

        # 화면 구성
        self.setup_main_menu()
        self.setup_login_screen()
        self.setup_create_account_screen()

    #로그인 할지 계정생성 할지 선택하는 페이즈
    def setup_main_menu(self):
        '''메인메뉴 화면 세팅'''
        tk.Label(self.main_menu_frame, text="선택하세요:").pack()
        tk.Button(self.main_menu_frame, text="로그인", command=self.switch_to_login).pack()
        tk.Button(self.main_menu_frame, text="계정 생성", command=self.switch_to_create_account).pack()

    #로그인 페이즈
    def setup_login_screen(self):
        '''로그인 화면 세팅'''
        tk.Label(self.login_frame, text="아이디:").grid(row=0, column=0)
        self.username_entry = tk.Entry(self.login_frame)    #빈 입력가능한 칸 생성
        self.username_entry.grid(row=0, column=1)

        tk.Label(self.login_frame, text="비밀번호:").grid(row=1, column=0)
        self.password_entry = tk.Entry(self.login_frame, show="*") #빈 입력가능한 칸 생성 입력시 *로 표시됨됨
        self.password_entry.grid(row=1, column=1)

        tk.Button(self.login_frame, text="로그인", command=self.login).grid(row=2, column=0, columnspan=2)  
        #로그인 함수를 사용하여 계정 로그인 확인을 하고 실패 성공 유무 왜 실패하였는지에 대한 정보를 받아 메세지 박스로 띄움
        tk.Button(self.login_frame, text="메인 메뉴로", command=self.switch_to_main_menu).grid(row=3, column=0, columnspan=2)   
        #메인 메뉴 페이즈로 화면 전환.

    #계정생성 페이즈
    def setup_create_account_screen(self):
        '''계정생성 화면 세팅'''
        #로그인 페이즈와 비슷함 생성 버튼이 계정생성 함수를 실행 시킬 뿐임.
        tk.Label(self.create_account_frame, text="아이디:").grid(row=0, column=0)
        self.new_username_entry = tk.Entry(self.create_account_frame)
        self.new_username_entry.grid(row=0, column=1)

        tk.Label(self.create_account_frame, text="비밀번호:").grid(row=1, column=0)
        self.new_password_entry = tk.Entry(self.create_account_frame, show="*")
        self.new_password_entry.grid(row=1, column=1)

        tk.Button(self.create_account_frame, text="생성", command=self.create_account).grid(row=2, column=0, columnspan=2)
        tk.Button(self.create_account_frame, text="메인 메뉴로", command=self.switch_to_main_menu).grid(row=3, column=0, columnspan=2)

    def switch_to_main_menu(self):
        '''메인메뉴로 화면 전환'''
        #화면 전환시 기존 화면은 지우고 새로운 화면을 나타내는 것이 좋음 에러가 안생김. 아래 switch frame 모두 동일일
        self.hide_all_frames()
        self.main_menu_frame.pack(expand=True)

    def switch_to_login(self):
        '''로그인로 화면 전환'''
        self.hide_all_frames()
        self.login_frame.pack(expand=True)

    def switch_to_create_account(self):
        '''계정생성으로 화면 전환'''
        self.hide_all_frames()
        self.create_account_frame.pack(expand=True)

    def hide_all_frames(self):
        '''모든 화면 숨기기'''
        self.main_menu_frame.pack_forget()
        self.login_frame.pack_forget()
        self.create_account_frame.pack_forget()

    def login(self):
        '''화면에 입력 받은 데이터 계정 매니저의 로그인 함수로 넘김 -> 수행후 내용 retrun받아 메시지 박스 생성'''
        username = self.username_entry.get()
        password = self.password_entry.get()
        #입력 받은 값을 login에 보내고 결과값을 받아 메시지 박스로 화면에 띄움
        result = self.account_manager.login(username, password)
        messagebox.showinfo("Login", result)

    def create_account(self):
        '''화면에 입력 받은 데이터 계정 매니저의 계정생성 함수로 넘김 -> 수행후 내용 retrun받아 메시지 박스 생성'''
        username = self.new_username_entry.get()
        password = self.new_password_entry.get()
        #입력 받은 값을 create_account에 보내고 결과값을 받아 메시지 박스로 화면에 띄움
        result = self.account_manager.create_account(username, password)
        messagebox.showinfo("Create Account", result)