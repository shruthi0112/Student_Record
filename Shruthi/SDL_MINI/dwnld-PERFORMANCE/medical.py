import numpy as np
import pandas as pd

medical_data = None

def read_medical_data():

    global medical_data
    medical_data = pd.read_csv("data/medical_data.csv")
    # print medical_data.head()

def history(reg_no):

    test = medical_data[medical_data.reg == reg_no]
    test = test[["date", "checkup"]]
    print (test)
