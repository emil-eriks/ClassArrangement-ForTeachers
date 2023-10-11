# This project will be annotated due to the fact it is an open source repository

#importing necessary modules 
import pandas as pd


# code
xls = pd.read_excel("C:\\Users\\user_name\\Desktop\\formatOfPronoteClassExcel.xlsx", engine='openpyxl')
print(xls.head())

name_data = xls["Nom"]

row = 5
column = 6

seating_plan = pd.DataFrame('Empty', index=range(1, row + 1), columns=range(1, column + 1))

for name in name_data:
    print(name)

print(seating_plan)

    