from tkinter import *
from basement import * # 추가예정
from add_cart import add_menu

# 메뉴별 버튼 
americano_img = PhotoImage(file="C:\\PythonTeamPJ\\PythonTeamPJ\\images\\ame.png")
cafelatte_img = PhotoImage(file="C:\\PythonTeamPJ\\PythonTeamPJ\\images\\cafla.png")
coldbrew_img = PhotoImage(file="C:\\PythonTeamPJ\\PythonTeamPJ\\images\\coldb.png")
# lemonade_img = PhotoImage(file="C:\\PythonTeamPJ\\PythonTeamPJ\\images\\lemonade.png") 추가예정정


cake_img = PhotoImage(file="C:\\PythonTeamPJ\\PythonTeamPJ\\images\\cak.png")
croissant_img = PhotoImage(file="C:\\PythonTeamPJ\\PythonTeamPJ\\images\\croissant.png")
# macaron_img = PhotoImage(file="C:\\PythonTeamPJ\\PythonTeamPJ\\images\\macaron.png")
# cookie_img = PhotoImage(file="C:\\PythonTeamPJ\\PythonTeamPJ\\images\\cookie.png")

americano_btn = Button(window, image=americano_img, text="아메리카노", command=lambda: add_menu("커피", "아메리카노")) # add_cart 추가 예정
cafelatte_btn = Button(window, image=cafelatte_img, text="카페라떼", command=lambda:add_menu("커피", "카페라떼"))
coldbrew_btn = Button(window,  image=coldbrew_img , text="콜드브루", command=lambda:add_menu("커피", "콜드브루"))
# lemonade_btn = Button(window,  image=lemonade_img , text="레모네이드", command=lambda:add_menu("커피", "레모네이드"))

cake_btn = Button(window, image=cake_img , text="케이크", command=lambda:add_menu("디저트", "케이크"))
croissant_btn = Button(window, image=croissant_img, text="크루아상", command=lambda:add_menu("디저트", "크루아상"))
# macaron_btn = Button(window, image=croissant_img, text="마카롱", command=lambda:add_menu("디저트", "마카롱"))
# cookie_btn = Button(window, image=croissant_img, text="쿠키", command=lambda:add_menu("디저트", "쿠키"))

def show_coffee() :
    global isCoffeeMenuOpen, isDessertMenuOpen 
    # 커피 메뉴 True, 디저트 메뉴 False
    isCoffeeMenuOpen = True
    isDessertMenuOpen = False
    
    # 커피 메뉴가 열려있을 때 -> 디저트 메뉴 닫기 / 커피 메뉴 열기
    if isDessertMenuOpen == False :
        cake_btn.place_forget()
        croissant_btn.place_forget()
        # macaron_btn.place_forget()
        # cookie_btn.place_forget()
        
    if isCoffeeMenuOpen == True :
        americano_btn.place(x=150, y=130)
        cafelatte_btn.place(x=300, y=130)
        coldbrew_btn.place(x=150, y=280)
        # lemonade_btn.place(x=300, y=280)  # 레모네이드 버튼 추가 예정
def show_dessert() :
    # 커피 메뉴 False, 디저트 메뉴 True
    isCoffeeMenuOpen = False
    isDessertMenuOpen = True
    
    # 디저트 메뉴가 열려있을 때 -> 커피 메뉴 닫기 / 디저트 메뉴 열기
    if isCoffeeMenuOpen == False :
        americano_btn.place_forget()
        cafelatte_btn.place_forget()
        coldbrew_btn.place_forget()
        # lemonade_btn.place_forget() 
        
    if isDessertMenuOpen == True :
        cake_btn.place(x=150, y=130)
        croissant_btn.place(x=300, y=130)
        # macaron_btn.place(x=150, y=280)
        # cookie_btn.place(x=300, y=280)
        
       
    
