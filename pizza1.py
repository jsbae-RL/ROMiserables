import tkinter as tk
from tkinter import messagebox

def calculate_total():
    # 가격 설정
    size_prices = {"Small": 17000, "Medium": 24000, "Large": 29000}
    topping_price = 2000

    # 선택된 크기와 토핑 수 계산
    size = size_var.get()
    num_toppings = sum(var.get() for var in topping_var.values())
    quantity = int(quantity_var.get())

    # 총합 계산
    if size in size_prices:
        total = (size_prices[size] + num_toppings * topping_price) * quantity
        total_label.config(text=f"Total: ${total:.2f}")
    else:
        messagebox.showerror("Error", "Please select a pizza size.")

def place_order():
    size = size_var.get()
    selected_toppings = [topping for topping, var in topping_var.items() if var.get() == 1]
    quantity = quantity_var.get()

    if not size:
        messagebox.showerror("Error", "Please select a pizza size.")
        return

    if int(quantity) <= 0:
        messagebox.showerror("Error", "Please enter a valid quantity.")
        return

    order_summary = (
        f"Order Summary:\n"
        f"Size: {size}\n"
        f"Toppings: {', '.join(selected_toppings) if selected_toppings else 'None'}\n"
        f"Quantity: {quantity}\n"
        f"Thank you for your order!"
    )

    messagebox.showinfo("Order Placed", order_summary)

# GUI 초기화
root = tk.Tk()
root.title("Pizza Order Program")
root.geometry("400x400")

# 피자 크기 선택
tk.Label(root, text="Select Pizza Size:").pack()
size_var = tk.StringVar(value="")

sizes = ["Small", "Medium", "Large"]
for size in sizes:
    tk.Radiobutton(root, text=size, variable=size_var, value=size).pack(anchor="w")

# 토핑 선택
tk.Label(root, text="Select Toppings:").pack()
topping_var = {
    "Pepperoni": tk.IntVar(),
    "Mushrooms": tk.IntVar(),
    "Onions": tk.IntVar(),
    "Sausage": tk.IntVar(),
    "Bacon": tk.IntVar()
}

for topping, var in topping_var.items():
    tk.Checkbutton(root, text=topping, variable=var).pack(anchor="w")

# 수량 선택
tk.Label(root, text="Enter Quantity:").pack()
quantity_var = tk.StringVar(value="1")
quantity_entry = tk.Entry(root, textvariable=quantity_var)
quantity_entry.pack()

# 계산 버튼
tk.Button(root, text="Calculate Total", command=calculate_total).pack()

# 총합 표시
total_label = tk.Label(root, text="Total: $0.00")
total_label.pack()

# 주문 버튼
tk.Button(root, text="Place Order", command=place_order).pack()

root.mainloop()
