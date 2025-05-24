import basement
from tkinter import *

def update():
    
    basement.cart_list.delete(0, END) # 장바구니 리스트박스 초기화
    total = 0
    
    for item in basement.cart :
        name = item[0]
        price = item[1]
        qty = item[2]
        total += price * qty
        basement.cart_list.insert(END, f"{name} - {price}원 x {qty}개")
    
    basement.total_label.config(text=f"총합계: {total}원")