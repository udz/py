# CRUD operation on Google Sheet
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
#scope = ['https://www.googleapis.com/auth/spreadsheets']
creds = ServiceAccountCredentials.from_json_keyfile_name('googlesheets/IMEPay_secret.json',scope)
client = gspread.authorize(creds)

sheet = client.open('IMEPay').sheet1

'''
#imepay = sheet.get_all_records()
imepay = sheet.row_values(1)
colval = sheet.col_values(2)
cellval = sheet.cell(2,2).value
sheet.update_cell(2,2,'987')

pprint.pprint(imepay)
pprint.pprint(colval)
pprint.pprint(cellval)
cellval = sheet.cell(2,2).value
pprint.pprint(cellval)
'''

row = [5,'98087878','Ujjwal',989789,32,43,'20187364767']
index = 6
#sheet.insert_row(row,index)

#sheet.delete_row(index)
row = str(sheet.row_count)
col = str(sheet.col_count)
print('Row Count is: ' + row + '\nCol Count: ' + col)
