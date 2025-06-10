from tkinter import *
from basement import * # 추가예정
from add_cart import add_menu

# 메뉴별 버튼 
americano_img = PhotoImage(file="C:\\PythonTeamPJ\\PythonTeamPJ\\images\\americano.png")
cafelatte_img = PhotoImage(file="C:\\PythonTeamPJ\\PythonTeamPJ\\images\\caffelatte.png")
coldbrew_img = PhotoImage(file="C:\\PythonTeamPJ\\PythonTeamPJ\\images\\coldbrew.png")
lemonade_img = PhotoImage(file="C:\\PythonTeamPJ\\PythonTeamPJ\\images\\lemonade.png") 


cake_img = PhotoImage(file="C:\\PythonTeamPJ\\PythonTeamPJ\\images\\cake.png")
croissant_img = PhotoImage(file="C:\\PythonTeamPJ\\PythonTeamPJ\\images\\croissant.png")
macaron_img = PhotoImage(file="C:\\PythonTeamPJ\\PythonTeamPJ\\images\\macaron.png")
cookie_img = PhotoImage(file="C:\\PythonTeamPJ\\PythonTeamPJ\\images\\cookie.png")

americano_btn = Button(window, image=americano_img, command=lambda: add_menu("커피", "아메리카노")) # add_cart 추가 예정
cafelatte_btn = Button(window, image=cafelatte_img, command=lambda:add_menu("커피", "카페라떼"))
coldbrew_btn = Button(window,  image=coldbrew_img , command=lambda:add_menu("커피", "콜드브루"))
lemonade_btn = Button(window,  image=lemonade_img , command=lambda:add_menu("커피", "레몬에이드"))

cake_btn = Button(window, image=cake_img , text="케이크", command=lambda:add_menu("디저트", "케이크"))
croissant_btn = Button(window, image=croissant_img, text="크루아상", command=lambda:add_menu("디저트", "크루아상"))
macaron_btn = Button(window, image=macaron_img, text="마카롱", command=lambda:add_menu("디저트", "마카롱"))
cookie_btn = Button(window, image=cookie_img, text="쿠키", command=lambda:add_menu("디저트", "쿠키"))

americano_price = Label(window, text="아메리카노 : 2000원")
cafelatte_price = Label(window, text="카페라떼 : 3000원")
coldbrew_price = Label(window, text="콜드브루 : 4000원")
lemonade_price = Label(window, text="레몬에이드 : 3500원")

cake_price = Label(window, text="케이크 : 5000원")
croissant_price = Label(window, text="크루아상 : 4000원")
macaron_price = Label(window, text="마카롱 : 2500원")
cookie_price = Label(window, text="쿠키 : 2000원")

def show_coffee() :
    global isCoffeeMenuOpen, isDessertMenuOpen 
    # 커피 메뉴 True, 디저트 메뉴 False
    isCoffeeMenuOpen = True
    isDessertMenuOpen = False
    
    # 커피 메뉴가 열려있을 때 -> 디저트 메뉴 닫기 / 커피 메뉴 열기
    if isDessertMenuOpen == False :
        cake_btn.place_forget()
        croissant_btn.place_forget()
        macaron_btn.place_forget()
        cookie_btn.place_forget()

        cake_price.place_forget()
        croissant_price.place_forget()
        macaron_price.place_forget()
        cookie_price.place_forget()

        
    if isCoffeeMenuOpen == True :
        americano_btn.place(x=150, y=130)
        cafelatte_btn.place(x=300, y=130)
        coldbrew_btn.place(x=150, y=280)
        lemonade_btn.place(x=300, y=280)  # 레모네이드 버튼 추가 예정
        
        americano_price.place(x=150, y=250)
        cafelatte_price.place(x=305, y=250)
        coldbrew_price.place(x=155, y=400)
        lemonade_price.place(x=300, y=400)
        
        
def show_dessert() :
    # 커피 메뉴 False, 디저트 메뉴 True
    isCoffeeMenuOpen = False
    isDessertMenuOpen = True
    
    # 디저트 메뉴가 열려있을 때 -> 커피 메뉴 닫기 / 디저트 메뉴 열기
    if isCoffeeMenuOpen == False :
        americano_btn.place_forget()
        cafelatte_btn.place_forget()
        coldbrew_btn.place_forget()
        lemonade_btn.place_forget()

        americano_price.place_forget()
        cafelatte_price.place_forget()
        coldbrew_price.place_forget()
        lemonade_price.place_forget() 
        
    if isDessertMenuOpen == True :
        cake_btn.place(x=150, y=130)
        croissant_btn.place(x=300, y=130)
        macaron_btn.place(x=150, y=280)
        cookie_btn.place(x=300, y=280)

        cake_price.place(x=155, y=250)
        croissant_price.place(x=305, y=250)
        macaron_price.place(x=163, y=400)
        cookie_price.place(x=315, y=400)
        
       
    
