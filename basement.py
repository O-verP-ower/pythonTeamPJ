from tkinter import *

# 제목 / 해상도 / 사이즈 조정 관련 지정
window = Tk()
window.title("카페 키오스크")
window.geometry("500x700")
window.resizable(False, False)
window.protocol("WM_DELETE_WINDOW", lambda: quit())

payment = Tk()
payment.title("결제")
payment.geometry("300x150")
payment.resizable(False, False)
payment.withdraw()
payment.protocol("WM_DELETE_WINDOW", lambda: payment.withdraw())

purchase = Tk()
purchase.title("결제")
purchase.geometry("200x100")
purchase.resizable(False, False)
purchase.withdraw()
purchase.protocol("WM_DELETE_WINDOW", lambda: purchase.withdraw())


# 메뉴 구성
menu = {
    "커피": {
        "아메리카노": 2000,
        "카페라떼": 3000,
        "콜드브루": 4000,
        "레몬에이드" : 3500,
    },
    "디저트": {
        "케이크": 5000, 
        "크루아상": 4000,
        "마카롱": 2500,
        "쿠키": 2000,
    }
}


cart = []  # 장바구니
waiting_number = 1  # 대기번호 -> 차후 개발 예정

# UI 위젯들 초기값 None으로 선언
total_label = None
cart_list = None

isCoffeeMenuOpen = None
isDessertMenuOpen = None

While_pay = None
Info = None