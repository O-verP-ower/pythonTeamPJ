from basement import *
from tkinter import messagebox as msg
from update import *
from receipt import *
from waiting_number import *

def checkout():
        receipt() # 영수증 출력 후 장바구니 초기화 -> 5/28 픽스
        cart.clear() 
        update()
        print_number()
        basement.waiting_number += 1
    