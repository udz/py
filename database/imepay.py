
# Connect
import pyodbc
#server = '192.168.1.47' 
server = '10.1.1.145'
database = 'WALLET_CORE_STAGING'
username = 'sa'
password = 'sasa'
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

print('Connection Success')


# Sample select query
cursor.execute("SELECT TOP 10 * FROM dbo.SW_TBL_PROFILE_CUST (NOLOCK) ORDER BY Created_Date DESC")
row = cursor.fetchone()
while row:
    string = ""
    i=0
    for j in range(len(row) - 1):
        if i==0:
            string = str(row[0])
        else:
            string += ',' + str(row[i])
        #print(str(i) + ' - ' + string)
        i+=1
    #print(str(row[0]) + ',' + row[1] + ',' + str(row[2]) + ',' + str(row[3])+ ',' + str(row[4]))
    print(string + '\n')
    row = cursor.fetchone()


'''
#Sample insert query
cursor.execute("INSERT SalesLT.Product (Name, ProductNumber, StandardCost, ListPrice, SellStartDate) OUTPUT INSERTED.ProductID VALUES ('SQL Server Express New 20', 'SQLEXPRESS New 20', 0, 0, CURRENT_TIMESTAMP )") 
row = cursor.fetchone()

while row: 
    print('Inserted Product key is ' + str(row[0]))
    row = cursor.fetchone()
'''
cnxn.close()

