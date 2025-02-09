# 음료 주문 프로그램

# menu={'coffee':3500,'latte':4000,'smoothie':5000,'tea':3000}

# 해당 딕셔너리를 활용하여 음료 주문을 하는 GUI프로그램을 생성한다.
# 창 제목은 음료 주문 프로그램이라고 작성한다.
# exit버튼을 누르면 터미널에 음료 주문 프로그램을 종료했다는 문구와 함께 프로그램 창을 종료시킨다.
# 창에는 메뉴판에 있는 메뉴명을 기재하며 각 메뉴 버튼을 누르면 하단에 총 금액과 총 가격에 반영되도록 이벤트를 설정한다.
from tkinter import Tk
from tkinter import Button
from tkinter import Label

menu={'coffee':3500,'latte':4000,'smoothie':5000,'tea':3000}
menu_list = list(menu.keys())
sum = 0

def event(key):
    global sum
    sum += menu[key]
    
    olabel3 = Label(otk, text=f'{key}: {menu[key]}원')
    olabel3.pack()
    olabel4['text']=f'총 {sum}원'

otk = Tk()
otk.title('음료 주문 프로그램')
otk.geometry('300x300+200+200')

exitbotton = Button(otk, text='exit',command=exit)
exitbotton.pack(side='bottom')

olabel1 = Label(otk, text='<Menu>')
olabel1.pack(side='top')

obtn1 = Button(otk, text=menu_list[0], width=10 ,command=lambda: event(menu_list[0]))
obtn2 = Button(otk, text=menu_list[1], width=10 ,command=lambda: event(menu_list[1]))
obtn3 = Button(otk, text=menu_list[2], width=10 ,command=lambda: event(menu_list[2]))
obtn4 = Button(otk, text=menu_list[3], width=10 ,command=lambda: event(menu_list[3]))

obtn1.pack()
obtn2.pack()
obtn3.pack()
obtn4.pack()

olabel2 = Label(otk, text='주문내역')
olabel4 = Label(otk, text=f'총 {sum}원')

olabel2.pack()
olabel4.pack(side='bottom')

otk.mainloop()