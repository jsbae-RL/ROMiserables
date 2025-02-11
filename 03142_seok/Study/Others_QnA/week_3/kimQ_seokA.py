# 음료 주문 프로그램

# menu={'coffee':3500,'latte':4000,'smoothie':5000,'tea':3000}

# 해당 딕셔너리를 활용하여 음료 주문을 하는 GUI프로그램을 생성한다.
# 창 제목은 음료 주문 프로그램이라고 작성한다.
# exit버튼을 누르면 터미널에 음료 주문 프로그램을 종료했다는 문구와 함께 프로그램 창을 종료시킨다.
# 창에는 메뉴판에 있는 메뉴명을 기재하며 각 메뉴 버튼을 누르면 하단에 총 금액과 총 가격에 반영되도록 이벤트를 설정한다.

from tkinter import *

oroot=Tk()
oroot.title("음료 주문 프로그램")
oroot.geometry("350x540")
order_text = StringVar()
order_text.set("총 주문 금액: 0원")

menu={ "coffee" : 3500, "latte" : 4000, "smoothie" : 5000, "tea" : 3000 }
total_price = 0
def order(name):
    global total_price
    total_price += menu[name]
    order_text.set(f"총 주문 금액: {total_price}원")
 

def exit_order():
    print("음료 주문 프로그램을 종료했습니다.")
    oroot.quit()

subs_x, subs_y = 3, 3   # 이미지 크기 조정값(subsample 사용)
btn_w, btn_h = 150, 180 # 버튼 크기 조정값

coffee_img =    PhotoImage(file=r"C:\Users\LDS\Desktop\ROMiserables\03142_seok\study_week_3\kim\coffee.png").subsample(subs_x,subs_y)
latte_img =     PhotoImage(file=r"C:\Users\LDS\Desktop\ROMiserables\03142_seok\study_week_3\kim\latte.png").subsample(subs_x,subs_y)
smoothie_img =  PhotoImage(file=r"C:\Users\LDS\Desktop\ROMiserables\03142_seok\study_week_3\kim\smoothie.png").subsample(subs_x,subs_y)
tea_img =       PhotoImage(file=r"C:\Users\LDS\Desktop\ROMiserables\03142_seok\study_week_3\kim\tea.png").subsample(subs_x,subs_y)

coffee_btn =    Button(oroot, text="coffee\n \\3500",   image = coffee_img,     width = btn_w, height = btn_h, compound = "top", command = lambda : order("coffee"))
latte_btn =     Button(oroot, text="latte\n \\4000",    image = latte_img,      width = btn_w, height = btn_h, compound = "top", command = lambda : order("latte"))
smoothie_btn =  Button(oroot, text="smoothie\n \\5000", image = smoothie_img,   width = btn_w, height = btn_h, compound = "top", command = lambda : order("smoothie"))
tea_btn =       Button(oroot, text="tea\n \\3000",      image = tea_img,        width = btn_w, height = btn_h, compound = "top", command = lambda : order("tea"))
exit_btn =      Button(oroot, text="exit", width = 45, height = 0, command = exit_order)

olabel = Label(oroot, textvariable = order_text, width = 45, height = 5, bg = "beige", relief = "raised")

coffee_btn.place    (x = 10, y = 10)
latte_btn.place     (x = 180, y = 10)     
smoothie_btn.place  (x = 10, y = 210) 
tea_btn.place       (x = 180, y = 210)     
exit_btn.place      (x = 12, y = 503)
olabel.place        (x = 13, y = 410)

oroot.mainloop()