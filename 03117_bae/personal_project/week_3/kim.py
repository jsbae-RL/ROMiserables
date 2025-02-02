import tkinter as tk
from tkinter import messagebox

# 음료 메뉴 및 가격
menu = {'Coffee': 3500, 'Latte': 4000, 'Smoothie': 5000, 'Tea': 3000}

# 총 금액 초기화
total_price = 0

# 주문한 음료를 추가하는 함수
def add_order(drink):
    global total_price  # 전역 변수 사용 선언
    order_list.insert(tk.END, f"{drink} - {menu[drink]}₩")  # 주문 목록에 추가
    total_price += menu[drink]  # 총 금액 업데이트
    total_label.config(text=f"총 금액: {total_price}₩")  # 총 금액 표시 업데이트

# 프로그램 종료 함수
def exit_program():
    print("음료 주문 프로그램이 종료되었습니다.")  # 터미널에 종료 메시지 출력
    root.destroy()  # GUI 창 닫기

# 메인 윈도우 생성
root = tk.Tk()
root.title("음료 주문 프로그램")  # 창 제목 설정
root.geometry("350x400")  # 창 크기 설정

# 메뉴 제목 라벨
menu_label = tk.Label(root, text="메뉴", font=("Arial", 14, "bold"))
menu_label.pack()

# 메뉴 버튼을 담을 프레임 생성
menu_frame = tk.Frame(root)
menu_frame.pack()

# 각 음료 메뉴에 대한 버튼 생성
for drink, price in menu.items():
    btn = tk.Button(menu_frame, text=f"{drink} ({price}₩)", width=15, command=lambda d=drink: add_order(d))
    btn.pack(pady=2)  # 버튼 간격 설정

# 주문 목록을 표시할 리스트박스 생성
order_list = tk.Listbox(root, width=30, height=10)
order_list.pack(pady=10)

# 총 금액을 표시할 라벨
total_label = tk.Label(root, text="총 금액: 0₩", font=("Arial", 12, "bold"))
total_label.pack()

# 종료 버튼 생성
exit_button = tk.Button(root, text="EXIT", width=10, bg="red", fg="white", command=exit_program)
exit_button.pack(pady=10)

# 메인 이벤트 루프 실행
root.mainloop()