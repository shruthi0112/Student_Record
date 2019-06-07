import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

marks_data = None

def read_marks_data():

    global marks_data
    marks_data = pd.read_csv("data/marks_data.csv")
    # print attendance_data

def disp_marks(reg_no):

    test = marks_data[marks_data.reg == reg_no]
    lab = list(test.columns.values)[1:]
    test = test.iloc[:, 1:].values.tolist()[0]
    print (test)
    print (lab)

    y = []
    for each in test:
        lst = map(int, each.split(' '))
        for i in lst:
            y.append(i)
    # print y

    fig, ax = plt.subplots()
    width = 0.75
    ind = np.arange(len(y))
    ax.bar(ind[::4], y[::4], width, label='CAT1', color="blue")
    ax.bar(ind[1::4], y[1::4], width, label='CAT2', color="red")
    ax.bar(ind[2::4], y[2::4], width, label='DA', color="green")
    ax.bar(ind[3::4], y[3::4], width, label='FAT', color="black")
    ax.set_xticks(ind[1::4]+width)
    ax.set_xticklabels(lab, minor=False)
    ax.legend(loc='best')
    plt.title("Marks")
    plt.xlabel("Subjects")
    plt.ylabel("Score")
    plt.show()
