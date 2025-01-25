import tkinter as tk
from src.gui_screens import GUIScreens

#if __name__ == "__main__": 하면 분리된 py.가 잘못된 연결을 안하도록 할 수 있다고 함. 안해도 잘되서 안씀
root = tk.Tk()
root.title("Account Management")
root.geometry("300x150")
#위는 잘알꺼같아서 안씀 아래는 음 root로 gui를 열어서 제어는 app으로 연결하여 가능하다는 정도. GUI가보면 애초에 root 입력 받게 되어있음.
app = GUIScreens(root)  #root 입력 안하면 연결안되서 제어 못함.
app.switch_to_main_menu()   #시작 화면은 메인 메뉴 화면이라서 먼저 부름.

root.mainloop()