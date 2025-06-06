from tkinter import *
from tkinter import messagebox as msg
from basement import *
from checkout import *

def cardOrCash():
     
    # 장바구니가 비어 있는 경우
    if not cart :
        msg.showinfo("알림", "장바구니가 비었습니다.")
        return
    payment.deiconify()  # 결제 창 보이기
    
def keyEvent(event) :
    
    global While_pay
    
    if event.keycode == 13:
        if While_pay is None :
            While_pay = Label(purchase, text="결제 중.....")
            While_pay.pack()
        else :
            While_pay.config(text="결제 중.....")
        purchase.after(2000,complete)
        
    else :
        msg.showwarning("오류", "결제가 제대로 완료되지 않았습니다.")
            
            
        
def card_pay():
    
    global Info
    
    purchase.deiconify()
    if Info is None :
            Info = Label(purchase, text="카드를 넣어주세요.(Enter)")
            Info.pack()
    else :
            Info.config(text="카드를 넣어주세요.(Enter)")
    purchase.bind("<Key>", keyEvent)
    purchase.focus_set()
    
    
def cash_pay():
    
    global Info
    
    purchase.deiconify()
    if Info is None :
            Info = Label(purchase, text="현금을 투입해 주세요.(Enter)")
            Info.pack()
    else :
            Info.config(text="현금을 투입해 주세요.(Enter) ")
    purchase.bind("<Key>", keyEvent)
    purchase.focus_set()
    
    
def complete():
        global While_pay
        msg.showinfo("알림", "결제가 완료되었습니다.")
        purchase.withdraw()
        payment.withdraw()
        While_pay.pack_forget()
        While_pay = None
        checkout()
        
    