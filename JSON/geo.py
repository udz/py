import openpyxl

wb = openpyxl.load_workbook('JSON/geo.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')



local_units = []
for rowOfCellObjects in sheet['B2':'B754']:
    i = 0
    for cellObj in rowOfCellObjects:
        local_units.insert(i,cellObj.value)
        #print(cellObj.value)
        i+=1
j = len(local_units) -1
print(j)
values3 = []
i = 0
while i < len(local_units): 
#for value in values2:
    value = "'" + local_units[j] + "',"
    print(value + ' ' + str(j))
    values3.insert(j,value)
    j -= 1
    i += 1
 
with open('JSON/test.txt','w') as file:
    file.truncate()
    file.writelines(values3)
print('\n\n')
print(values3[0])
print(values3[1])
#print(values2)

