import numpy as np
import pandas as pd

login_data = None

def read_login_data():

    global login_data
    login_data = pd.read_csv("data\login_data.csv")
    # print login_data.head()

def try_login():

    uname = input('Enter Username : ')
    password = input('Enter Password : ')
    if uname in list(login_data["name"]):
        test = login_data[login_data.name == uname]
        if password == list(test.password)[0]:
            return True, list(test.reg)[0]
    return False, None
