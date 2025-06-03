import basement
from tkinter import *
from tkinter import messagebox as msg
import shows_menu
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

def cancel_all():
    
    if not basement.cart:
            msg.showinfo("알림", "장바구니가 비었습니다.")
            return
    
    else:
            answer = msg.askyesno("알림", "전체 취소하시겠습니까?")

            if answer == 1:
                basement.cart.clear()
                update()
                shows_menu.show_coffee()
            
            else :
                return
    
    

