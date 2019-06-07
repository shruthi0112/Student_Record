import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline
excel_file = 'C:\\Users\\SHRUTHI BHAT\\Desktop\\Shruthi\\XLSM\\CMks.xlsx'
marks = pd.read_excel(excel_file)
marks.head()

#DBMS MARKS ANALYSIS

sorted_by_dbms = marks.sort_values(['DBMS'], ascending=False)
sorted_by_dbms["DBMS"].head(10)
sorted_by_dbms['DBMS'].head(10).plot(kind="barh")
#plt.xlabel("")
#plt.ylabel("")
plt.title('DBMS SCORE ANALYSIS')
plt.show()
sorted_by_dbms['DBMS'].plot(kind="hist")
plt.show()
marks_subset = marks[['Roll-No', 'DBMS']]
marks_subset.head() 
#TOC MARKS ANALYSIS
sorted_by_toc = marks.sort_values(['TOC'], ascending=False)
sorted_by_toc["TOC"].head(10)
sorted_by_toc['TOC'].head(10).plot(kind="barh")
plt.title('TOC SCORE ANALYSIS')
plt.show()
sorted_by_toc['TOC'].plot(kind="hist")
plt.show()
#CN MARKS ANALYSIS
sorted_by_cn = marks.sort_values(['CN'], ascending=False)
sorted_by_cn["CN"].head(10)
sorted_by_cn['CN'].head(10).plot(kind="barh")
plt.title('CN SCORE ANALYSIS')
plt.show()
sorted_by_cn['CN'].plot(kind="hist")
plt.show
#SEPM MARKS ANALYSIS
sorted_by_sepm = marks.sort_values(['SEPM'], ascending=False)
sorted_by_sepm["SEPM"].head(10)
sorted_by_sepm['SEPM'].head(10).plot(kind="barh")
plt.title('SEPM SCORE ANALYSIS')
plt.show()
sorted_by_sepm['SEPM'].plot(kind="hist")
plt.show()
#ISEE MARKS ANALYSIS
sorted_by_isee = marks.sort_values(['ISEE'], ascending=False)
sorted_by_isee["ISEE"].head(10)
sorted_by_isee['ISEE'].head(10).plot(kind="barh")
plt.title('ISEE SCORE ANALYSIS')
plt.show() 
sorted_by_isee['ISEE'].plot(kind="hist")
plt.show()
#SWICH
