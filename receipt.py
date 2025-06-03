import datetime
from basement import *
from tkinter import *
from tkinter import messagebox as msg

def receipt():
    
    outFp = None
    choice = msg.askyesno("알림", "영수증을 출력하시겠습니까?")
    
    if choice == 1 :
        
        outFp = open("C:\\pythonTeamPJ\\pythonTeamPJ\\receipt\\receipt%s.txt" % datetime.datetime.now().strftime("%Y_%m_%d %H-%M-%S"), "w", encoding="utf-8")
        outFp.write("영수증\n")
        outFp.write("=========================\n")
        for item in cart :
            outFp.write("%s x %d개 - %d원\n" % (item[0], item[2], (item[1] * item[2])))
        # 총액 : %d원 출력되도록 구현 완료 (5/28)
        outFp.write("-------------------------\n")
        outFp.write("총액 : %d원\n" % sum([item[1] * item[2] for item in cart]))
        outFp.write("=========================\n")
        outFp.write("결제일시 : %s\n" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    else :
        pass
    
    