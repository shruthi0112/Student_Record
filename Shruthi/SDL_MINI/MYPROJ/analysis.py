import pandas as pd
import matplotlib.pyplot as plt
import xlrd
#%matplotlib inline
excel_file = 'CMks.xlsx'
marks = pd.read_excel('C:\\Users\\SHRUTHI BHAT\\Desktop\\SDL_MINI\\CMks.xlsx')
#%matplotlib inline
excel_file = 'C:\\Users\SHRUTHI BHAT\Desktop\SDL_MINI\CMks.xlsx'
marks = pd.read_excel(excel_file)
marks.head()
'''
#DBMS MARKS ANALYSIS
def dbms_analysis(s):
        print("heyyy")
	sorted_by_dbms = marks.sort_values(['Roll-No'],ascending=True)
	sorted_by_dbms[s].head(10)
	sorted_by_dbms[s].head(10).plot(kind="barh")
	plt.show()
	sorted_by_dbms[s].plot(kind="hist")
	plt.show()
	marks_subset = marks[['Roll-No',s]]
	marks_subset.head()
	
#SWICH
print ("ENTER YOUR CHOICE:")
ch = input()
if ch=="1":
        dbms_analysis('DBMS')
elif ch=="2":
        dbms_analysis('TOC')
elif ch=="3":
        dbms_analysis('CN')
        
'''
#######CLASSWISE ANALYSIS##########
sorted_by_dbms = marks.sort_values(['Roll-No'],ascending=True)
print(sorted_by_dbms)
sorted_by_dbms.plot.bar(x='Name')
plt.legend()
plt.show()
#--------------------------------------------------
activities = ['BELOW 12', '12-18', '19-25', 'ABOVE 25']
s="TOC"
c1=0
c2=0
c3=0
c4=0
book=xlrd.open_workbook('C:\\Users\\SHRUTHI BHAT\\Desktop\\SDL_MINI\\CMks.xlsx')
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
''' if i>0:
        if row[4]<12 and row[4]>=0:
            c1=c1+1
        if row[4]>=12 and row[4]<=18:
            c2=c2+1
        if row[4]>=19 and row[4]<=25:
            c3=c3+1
        if row[4]>25:
            c4=c4+1'''
print(c1,c2,c3,c4)
'''
# portion covered by each label 
slices = [c1, c2, c3, c4] 

# color for each label 
colors = ['r', 'y', 'g', 'b'] 
  
# plotting the pie chart 
plt.pie(slices, labels = activities, colors=colors,  
        startangle=90, shadow = True, explode = (0, 0, 0.1, 0), 
        radius = 1.2, autopct = '%1.1f%%') 
print(c1,c2,c3,c4) 
# plotting legend 
plt.legend() 
  
# showing the plot 
plt.show()'''
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

