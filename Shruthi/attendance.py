import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

final_attendance = None

def read_final_attendance():

    global final_attendance
    final_attendance = pd.read_csv("C:\\Users\\SHRUTHI BHAT\\Desktop\\Shruthi\\data\\final_attendance.csv")
    # print attendance_data

def disp_attendance(reg_no):

    test = final_attendance[final_attendance.Roll_No == reg_no]
    lab = list(test.columns.values)[1:]
    test = test.iloc[:, 1:].values.tolist()[0]
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
