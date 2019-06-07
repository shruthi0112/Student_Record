from tkinter import *
from medical import history, read_medical_data
from attendance import read_final_attendance, disp_attendance
from performance import read_performance_data, analyse_data
from marks import read_marks_data, disp_marks
#import analysis as anal
import os
import marks as ms
import main as mn
import displayform as df
import analysis as an

#main
main=Tk()
main.title("Main Menu")
main.geometry("800x400")

reg_no='16BCE2003'
#font
FONTT = ("Times", "22", "bold")
FONTT1 = ("Times", "15","bold")
#menu Button
#main label
Label(main,text="Main Menu",padx=0,pady=30,font=FONTT).grid(row=0,column=1,sticky=W)

#buttons group
Button(main,text="Insert Record",padx=50,pady=15,width=25,font=FONTT1,command = lambda:insert_record()).grid(row=1,column=0,sticky=W)
Button(main,text="Class Analysis ",padx=50,pady=15,width=25,font=FONTT1,command = lambda: analysis()).grid(row=1,column=1,sticky=W)
Button(main,text="Medical History",padx=50,pady=15,width=25,font=FONTT1,command = lambda:medical()).grid(row=2,column=0,sticky=W)
Button(main,text="Attendance",padx=50,pady=15,width=25,font=FONTT1,command = lambda:attendance()).grid(row=2,column=1,sticky=W)
Button(main,text="Student Marks",padx=50,pady=15,width=25,font=FONTT1,command = lambda:student_marks()).grid(row=3,column=0,sticky=W)
Button(main,text="Exit",padx=50,pady=15,width=25,font=FONTT1,command = lambda:quit()).grid(row=3,column=1,sticky=W)

#sub routine

def analysis():
  an.analysis()

def insert_record():
  os.system('python displayform.py')
    
def medical():
   mn.medical()

def attendance():
    mn.attendace()
    
def student_marks():
   mn.marks()

#mainloop
main.mainloop()
