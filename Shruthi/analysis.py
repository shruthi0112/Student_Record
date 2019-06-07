import pandas as pd
import matplotlib.pyplot as plt
import xlrd
def analysis():
    #
    excel_file = 'CMks.xlsx'
    marks = pd.read_excel('C:\\Users\\SHRUTHI BHAT\\Desktop\\Shruthi\\XLSM\\CMks.xlsx')
    #
    excel_file = 'C:\\Users\\SHRUTHI BHAT\\Desktop\\Shruthi\\XLSM\\CMks.xlsx'
    marks = pd.read_excel(excel_file)
    marks.head()
   
    ####### CLASSWISE ANALYSIS ######
    sorted_by_dbms = marks.sort_values(['Roll-No'],ascending=True)
    print(sorted_by_dbms)
    sorted_by_dbms.plot.bar(x='Name')
    plt.legend()
    plt.show()
    #--------------------------------------------------
    
    activities = ['BELOW 12', '12-18', '19-25', 'ABOVE 25']
    s="TOC"
    '''c1=0
    c2=0
    c3=0
    c4=0'''
    book=xlrd.open_workbook('C:\\Users\\SHRUTHI BHAT\\Desktop\\Shruthi\\XLSM\\CMks.xlsx')
    for sheet in book.sheets():
        print(sheet.name)
    '''for i in range(sheet.nrows):
        row=sheet.row_values(i)
        for cell in row:
            print(cell)'''
    count = 0

    for i in range(sheet.nrows):
        if count < 10:
            row = sheet.row_values(i)
            print(i, row)
            print(i, row[4])
            
        count += 1
        #print(row[4])
   
    #print(c1,c2,c3,c4)
   
    
    #----------------------------------------------------
    s="CN"
    marks = pd.read_excel(excel_file)
    mean_sub=marks[s].mean()
    print(mean_sub)

    s="DBMS"
    max_mar=marks[s].max(axis=0)
    print(max_mar)

    s="TOC"
    min_mar=marks[s].min()
    print(min_mar)

    s="DBMS"
    sorted_by_dec= marks.sort_values([s],ascending=False)
    print(sorted_by_dec)

