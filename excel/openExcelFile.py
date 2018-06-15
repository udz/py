import os
import openpyxl

cwd = os.getcwd()
print("Current Working Directory is" + cwd)

wb = openpyxl.load_workbook('excel/example.xlsx')
print(type(wb))
print(wb.get_sheet_names())
sheet = wb.get_sheet_by_name('Fruits')
print(sheet, type(sheet))
print(sheet['A1'].value)

c= sheet['B1']
print(c.coordinate + ' ' + c.value)

print(tuple(sheet['A1':'C3']))

print('*** Printing Values of each Cell ***')
for rowOfCellObjects in sheet['A1':'C3']:
    values = []
    i = 0
    for cellObj in rowOfCellObjects:
        values.insert(i,cellObj.value)
        i+=1
    print (values[:3])