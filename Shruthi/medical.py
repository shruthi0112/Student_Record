import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

medical_data = None

def read_medical_data():
    global df
    fields=["date","check up","reg"]
    df = pd.read_csv("C:\\Users\\SHRUTHI BHAT\\Desktop\\Shruthi\\data\\medical_data.csv",names=fields)
    # print medical_data.head()

def history(reg_no):
    
    print(df.groupby('date').size)
    df.groupby('date').size().plot(kind="bar")
    plt.show()
    
