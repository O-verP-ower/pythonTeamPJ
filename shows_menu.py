from tkinter import *
from basement import * # 추가예정
from add_cart import add_americano, add_caffeelatte, add_coldbrew, add_cake, add_croissant

# 메뉴별 버튼 
americano_btn = Button(window, text="아메리카노", width=10, command=add_americano) # add_cart 추가 예정
cafelatte_btn = Button(window, text="카페라떼",width=10, command=add_caffeelatte)
coldbrew_btn = Button(window,  text="콜드브루",width=10, command=add_coldbrew)
cake_btn = Button(window, text="케이크",width=10, command=add_cake)
croissant_btn = Button(window, text="크루아상",width=10, command=add_croissant)

def show_coffee() :
    global isCoffeeMenuOpen, isDessertMenuOpen 
    # 커피 메뉴 True, 디저트 메뉴 False
    isCoffeeMenuOpen = True
    isDessertMenuOpen = False
    
    # 커피 메뉴가 열려있을 때 -> 디저트 메뉴 닫기 / 커피 메뉴 열기
    if isDessertMenuOpen == False :
        cake_btn.place_forget()
        croissant_btn.place_forget()
        
    if isCoffeeMenuOpen == True :
        americano_btn.place(x=200, y=350)
        cafelatte_btn.place(x=300, y=350)
        coldbrew_btn.place(x=200, y=450)
def show_dessert() :
    # 커피 메뉴 False, 디저트 메뉴 True
    isCoffeeMenuOpen = False
    isDessertMenuOpen = True
    
    # 디저트 메뉴가 열려있을 때 -> 커피 메뉴 닫기 / 디저트 메뉴 열기
    if isCoffeeMenuOpen == False :
        americano_btn.place_forget()
        cafelatte_btn.place_forget()
        coldbrew_btn.place_forget()
        
    if isDessertMenuOpen == True :
        cake_btn.place(x=200, y=350)
        croissant_btn.place(x=300, y=350)
        
       
    
