import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

attendance_data = None

def read_attendance_data():

    global attendance_data
    attendance_data = pd.read_csv("data/attendance_data.csv")
    # print attendance_data

def disp_attendance(reg_no):

    test = attendance_data[attendance_data.reg == reg_no]
    lab = list(test.columns.values)[1:]
    test = test.iloc[1:].values.tolist()[1]
    print (test)
    print (lab)

    fig, ax = plt.subplots()
    width = 0.75
    ind = np.arange(len(test))
    ax.barh(ind, test, width, color="blue")
    ax.set_yticks(ind+width/2)
    ax.set_yticklabels(lab, minor=False)
    plt.title("Attendance")
    plt.xlabel("Percentage")
    plt.ylabel("Subjects")
    plt.show()
