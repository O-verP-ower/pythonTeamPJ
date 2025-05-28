from tkinter import *
from basement import * # 추가예정
from add_cart import add_americano, add_caffeelatte, add_coldbrew, add_cake, add_croissant

# 메뉴별 버튼 
americano_img = PhotoImage(file="C:\\PythonTeamPJ\\PythonTeamPJ\\images\\ame.png")
cafelatte_img = PhotoImage(file="C:\\PythonTeamPJ\\PythonTeamPJ\\images\\cafla.png")
coldbrew_img = PhotoImage(file="C:\\PythonTeamPJ\\PythonTeamPJ\\images\\coldb.png")
cake_img = PhotoImage(file="C:\\PythonTeamPJ\\PythonTeamPJ\\images\\cak.png")
croissant_img = PhotoImage(file="C:\\PythonTeamPJ\\PythonTeamPJ\\images\\croissant.png")

americano_btn = Button(window, image=americano_img, text="아메리카노", command=add_americano) # add_cart 추가 예정
cafelatte_btn = Button(window, image=cafelatte_img, text="카페라떼", command=add_caffeelatte)
coldbrew_btn = Button(window,  image=coldbrew_img , text="콜드브루", command=add_coldbrew)
cake_btn = Button(window, image=cake_img , text="케이크", command=add_cake)
croissant_btn = Button(window, image=croissant_img, text="크루아상", command=add_croissant)

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
        americano_btn.place(x=150, y=130)
        cafelatte_btn.place(x=300, y=130)
        coldbrew_btn.place(x=150, y=280)
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
        cake_btn.place(x=150, y=130)
        croissant_btn.place(x=300, y=130)
        
       
    
