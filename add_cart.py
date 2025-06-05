from basement import *
from update import *

# 메뉴별 추가 함수 구성 

def add_menu(category, name) : # 코드 간소화 (6/3)

    price = menu[category][name]
    
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
