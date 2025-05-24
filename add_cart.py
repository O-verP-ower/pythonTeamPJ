from basement import *
from update import *

# 메뉴별 추가 함수 구성 

def add_americano():
    name = "아메리카노"
    price = menu["커피"][name]
    _add_to_cart(name, price)

def add_caffeelatte():
    name = "카페라떼"
    price = menu["커피"][name]
    _add_to_cart(name, price)

def add_coldbrew():
    name = "콜드브루"
    price = menu["커피"][name]
    _add_to_cart(name, price)

def add_cake():
    name = "케이크"
    price = menu["디저트"][name]
    _add_to_cart(name, price)

def add_croissant():
    name = "크루아상"
    price = menu["디저트"][name]
    _add_to_cart(name, price)

# 공통 기능 함수 (내부에서만 사용)
def _add_to_cart(name, price):
    # 수량 = 1 / cart에 목록이 있는지 여부릁 통해 만약 같은 항목이 리스트에 있다면 수량만 증가
    qty = 1
    isThereInList = False

    for item in cart:
        if item[0] == name:
            item[2] += 1
            isThereInList = True
            
            break

    if not isThereInList:
        cart.append([name, price, qty])

    
    update()  # 장바구니 업데이트
