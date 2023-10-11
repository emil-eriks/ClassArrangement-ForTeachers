# This project will be annotated due to the fact it is an open source repository

#importing necessary modules 
import pandas as pd

# variables
seating_plan = None

# code
xls = pd.read_excel("C:\\Users\\Emil\\Desktop\\formatOfPronoteClassExcel.xlsx", engine='openpyxl')

row = 3
column = 3

name_data = xls["Nom"]
student_placement = []

def init_student_placement():
    for name in name_data:
        student_placement.append(name)
    
def init_dataframe():
    global seating_plan
    seating_plan = pd.DataFrame('Empty', index=range(1, row + 1), columns=range(1, column + 1))
    
def sort_into_table(name_data, row, column):
    i = 0
    for w in range(row):
        for l in range(column):
            if i >= len(student_placement):
                return 
            seating_plan.iloc[w, l] = student_placement[i]
            i += 1

init_student_placement()
init_dataframe()
sort_into_table(name_data, row, column)
seating_plan.to_excel('test2.xlsx', sheet_name='Seating Plan')