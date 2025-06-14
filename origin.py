import basement
from shows_menu import show_coffee, show_dessert
from tkinter  import *
from checkout import *
from cardOrCash import *

# UI 위젯 생성
# 커피 / 디저트 버튼 생성

coffee_btn = Button(basement.window, text="음료", width=10, command=show_coffee)
bakery_btn = Button(basement.window, text="디저트", width=10, command=show_dessert)
coffee_btn.place(x=175, y=30)
bakery_btn.place(x=295, y=30)

# 장바구니 생성 ( Listbox / 총합계 / 결제 버튼)
cart_list = Listbox(basement.window, width=30, height=10)
cart_list.place(x=170, y=450)
total_label = Label(basement.window, text="총합계 : 0원")
total_label.place(x=240, y=420)
checkout_btn = Button(basement.window, text="결제하기", width=10, bg='green', command=cardOrCash)
checkout_btn.place(x=200, y=650)

cancel_btn = Button(basement.window, text="전체 취소", width=10, bg='red', command=cancel_all)
cancel_btn.place(x=290, y=650)

# basement 모듈 내 변수에 현재 위젯 주소 할당
basement.cart_list = cart_list
basement.total_label = total_label

# 결제창 UI
payInfo = Label(payment, text="결제 방법을 선택하세요.")
payInfo.pack()
cardBtn = Button(payment, text="카드 결제", command=lambda: pay("card"))
cardBtn.place(x=75, y=50)
cashBtn = Button(payment, text="현금 결제", command=lambda: pay("cash"))
cashBtn.place(x=175, y=50)


# 초기 메뉴 커피로 설정
show_coffee()

basement.window.mainloop()
