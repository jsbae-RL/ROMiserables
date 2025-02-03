from tkinter import *

tk=Tk()

tk.title("order beverage")
tk.geometry("300x400")

menu={'coffee':3500,'latte':4000,'smoothie':5000,'tea':3000}

selected_quantity={}

total_quantity=IntVar()         #store selected beverage quantity
total_price=IntVar()            #store selected beverage price      #tkinter widget-data value sync
total_quantity.set(0)           #initial value=0(no select beverage)
total_price.set(0)

def show_order(item):           #when user press the button(beverage), call this function
    total_quantity.set(total_quantity.get()+1)              #get now quantity, and update +1
    total_price.set(total_price.get()+menu[item])           #get now price, and update with selected beverage price (menu[item]==bring selceted beverage's price)
    ostring.set(f"Total items: {total_quantity.get()} | Total price: {total_price.get()}won")  #store ostring with updated values

#ostring.set()method: update total qauntity and price
#total_quantity.get()=bring now total quantity
#total_price.get()=bring now total price

def order_exit():
    print("Order program exit")
    exit()
    
ostring=StringVar()
ostring.set("Total items: 0 | Total price: 0 won")      #default message

olabel=Label(tk,textvariable=ostring)                   #when ostirng update,label1 value update too
olabel.pack(side="bottom")

obtn1=Button(tk,text="coffee",width=10,height=1,command=lambda: show_order("coffee"))
obtn2=Button(tk,text="latte",width=10,height=1,command=lambda: show_order("latte"))
obtn3=Button(tk,text="smoothie",width=10,height=1,command=lambda:show_order("smoothie"))
obtn4=Button(tk,text="tea",width=10,height=1,command=lambda:show_order("tea"))
obtn5=Button(tk,text="exit",width=10,height=1,command=order_exit)

obtn1.pack(side="top")
obtn2.pack(side="top")
obtn3.pack(side="top")
obtn4.pack(side="top")
obtn5.pack(side="top")

tk.mainloop()