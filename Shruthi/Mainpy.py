import tkinter as tk
import tkinter.messagebox as tm
from tkinter import *
import sys
import numpy as np
import pandas as pd


login_data = None

FONTT = ("Times", "12", "bold italic")

class myApp(tk.Tk): 
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0,weight = 1)
        container.grid_columnconfigure(0,weight = 1)

        self.frames = {}

        frame = LoginPage(container,self)
        self.frames[LoginPage] = frame
        frame.grid(row = 0,column = 0,sticky = "nsew")

        self.show_frame(LoginPage)

    def show_frame(self,cont):

        frame = self.frames[cont]
        frame.tkraise()
       

def loginValidate(user,pwd):

    login_data = pd.read_csv("C:\\Users\\SHRUTHI BHAT\\Desktop\\Shruthi\\data\\login_data.csv")
    
    if user in list(login_data["name"]):
        test = login_data[login_data.name == user]
        if pwd == list(test.password)[0]:
            #open Menu
            import Start_From_here as sf
            
        else:
             tm.showerror("Login error", "Incorrect password")
    else:
        tm.showerror("Login error", "Incorrect username")

class LoginPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        usr_login = StringVar()
        pwd_login = StringVar()
        userLabel = tk.Label(self,text = "Name",font = FONTT )
        passwordLabel = tk.Label(self,text = "Password", font = FONTT)

        userEntry = tk.Entry(self, textvariable = usr_login, bd=5)
        passwordEntry = tk.Entry(self, textvariable=pwd_login,bd=5,show = "*")

        submitButton = tk.Button(self,text = "Login",command = lambda: loginValidate(usr_login.get(),pwd_login.get()))
        quitButton = tk.Button(self,text = "Quit",command =lambda: app.destroy)

        userLabel.grid(row = 0,sticky = "E",padx =10,pady =10)
        passwordLabel.grid(row =1,sticky = "E",padx =10,pady =10)
        userEntry.grid(row=0,column=1,padx =10,pady =10)
        passwordEntry.grid(row=1,column=1,padx =10,pady =10)
        submitButton.grid(row =2,column =1,padx =10,pady =10)
        quitButton.grid(row=2,column=2,padx =10,pady =10)

app = myApp()
app.mainloop()
