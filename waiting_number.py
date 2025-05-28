import basement
import datetime
from tkinter import messagebox as msg

def print_number():
    
    outFp = None
    outFp = open("C:\\pythonTeamPJ\\pythonTeamPJ\\waiting_number\\waiting_number%s.txt" % datetime.datetime.now().strftime("%Y_%m_%d %H-%M-%S"), "w", encoding="utf-8")
    outFp.write("영수증\n")
    outFp.write("==========================\n")
    outFp.write("대기번호 : %d\n" % basement.waiting_number)
    outFp.write("==========================\n")
    
    msg.showinfo("알림", "대기번호가 출력되었습니다. 대기번호는 %d번입니다!" % basement.waiting_number)
    