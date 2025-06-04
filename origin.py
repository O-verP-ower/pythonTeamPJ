import basement
from shows_menu import show_coffee, show_dessert
from tkinter  import *
from checkout import *

# UI 위젯 생성
# 커피 / 디저트 버튼 생성

coffee_btn = Button(basement.window, text="커피", width=10, command=show_coffee)
bakery_btn = Button(basement.window, text="디저트", width=10, command=show_dessert)
coffee_btn.place(x=175, y=30)
bakery_btn.place(x=295, y=30)

# 장바구니 생성 ( Listbox / 총합계 / 결제 버튼)
cart_list = Listbox(basement.window, width=30, height=10)
cart_list.place(x=170, y=450)
total_label = Label(basement.window, text="총합계 : 0원")
total_label.place(x=240, y=420)
checkout_btn = Button(basement.window, text="결제하기", width=10, bg='green', command=checkout)
checkout_btn.place(x=240, y=650)

# basement 모듈 내 변수에 현재 위젯 주소 할당
basement.cart_list = cart_list
basement.total_label = total_label

# 초기 메뉴 커피로 설정
show_coffee()

basement.window.mainloop()
