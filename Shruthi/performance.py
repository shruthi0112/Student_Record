import numpy as np
import pandas as pd

performance_data = None

def score(grade):

    if grade == 'S':
        return 10
    elif grade == 'A':
        return 9
    elif grade == 'B':
        return 8
    elif grade == 'C':
        return 7
    elif grade == 'D':
        return 6
    elif grade == 'E':
        return 5
    else:
        return 0

def read_performance_data():

    global performance_data
    performance_data = pd.read_csv("C:\\Users\\SHRUTHI BHAT\\Desktop\\Shruthi\\data\\performance_data.csv")
    # print performance_data

def analyse_data(reg_no):

    test = performance_data[performance_data.reg == reg_no]
    test = test.iloc[:, 1:].values.tolist()[0]
    print ("Grades : ",test)
    total = 0.0
    for i in test:
        total += score(i)
    print ("CGPA : ", round(total/len(test), 2))
