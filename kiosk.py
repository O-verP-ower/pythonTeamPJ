import tkinter as tk
from tkinter import messagebox

# 메뉴 데이터
menu = {
    "커피": {
        "아메리카노": 3000,
        "카페라떼": 3500,
        "바닐라라떼": 4000
    },
    "디저트": {
        "치즈케이크": 4500,
        "티라미수": 5000
    }
}

cart = []

# 주문 추가 함수
def add_to_cart(item_name, item_price):
    cart.append({"name": item_name, "price": item_price, "qty": 1})
    update_cart()

# 장바구니 갱신
def update_cart():
    cart_list.delete(0, tk.END)
    total = 0
    for item in cart:
        line = f"{item['name']} x {item['qty']} - {item['price']}원"
        cart_list.insert(tk.END, line)
        total += item["price"] * item["qty"]
    total_label.config(text=f"총합계: {total}원")

# 결제 함수
def checkout():
    if not cart:
        messagebox.showinfo("알림", "장바구니가 비어 있습니다.")
        return
    total = sum(item["price"] * item["qty"] for item in cart)
    messagebox.showinfo("결제 완료", f"총 {total}원이 결제되었습니다.\n감사합니다!")
    cart.clear()
    update_cart()

# 카테고리 변경
def show_menu(category):
    for widget in menu_frame.winfo_children():
        widget.destroy()
    for item, price in menu[category].items():
        btn = tk.Button(menu_frame, text=f"{item} ({price}원)", width=20,
                        command=lambda n=item, p=price: add_to_cart(n, p))
        btn.pack(pady=2)

# 메인 윈도우
root = tk.Tk()
root.title("카페 키오스크")
root.geometry("500x400")

# 카테고리 버튼
top_frame = tk.Frame(root)
top_frame.pack(pady=10)

tk.Button(top_frame, text="커피", width=10, command=lambda: show_menu("커피")).pack(side=tk.LEFT, padx=10)
tk.Button(top_frame, text="디저트", width=10, command=lambda: show_menu("디저트")).pack(side=tk.LEFT, padx=10)

# 메뉴 영역
menu_frame = tk.Frame(root)
menu_frame.pack(pady=10)

# 장바구니
cart_frame = tk.Frame(root)
cart_frame.pack(pady=10)

tk.Label(cart_frame, text="장바구니").pack()
cart_list = tk.Listbox(cart_frame, width=40, height=6)
cart_list.pack()

total_label = tk.Label(cart_frame, text="총합계: 0원")
total_label.pack(pady=5)

tk.Button(root, text="결제하기", bg="green", fg="white", width=20, command=checkout).pack(pady=10)

# 초기 메뉴 출력
show_menu("커피")

root.mainloop()
