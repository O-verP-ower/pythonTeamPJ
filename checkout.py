from basement import *
from tkinter import messagebox as msg
from update import *
from receipt import *
from waiting_number import *
def checkout() :
    
    # 장바구니가 비어 있는 경우
    if not cart :
        msg.showinfo("알림", "장바구니가 비었습니다.")
        return
        
    # 장바구니가 비어 있지 않은 경우 -> 결제 완료 메세지 출력 (차후 영수증 출력 여부 + 대기번호 출력 예정)
    msg.showinfo("알림", "결제가 완료되었습니다!")
    # 장바구니 초기화
    receipt() # 영수증 출력 후 장바구니 초기화 -> 5/28 픽스
    cart.clear() 
    update()
    print_number()
    basement.waiting_number += 1
    