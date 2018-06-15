import os
import json
import pprint

# Print CWD
cwd = os.getcwd()
#print("Current Working Directory is" + cwd)

file1 = open('JSON/data.json', "r")
#wb = openpyxl.load_workbook('JSON/DomesticFlight.xlsx')
#sheet = wb.get_sheet_by_name('Sheet2')

file = open('JSON/output1.csv','w')
header = ('Line#,Adult,Airline,Arrival,Departure,FlightClassCode,AdultFare,ChildFare,AgencyCommission,ChildCommission,GrandTotal')
pprint.pprint(header,file)

for line in file1:
#for m in range (4,866):
    #jsonValue = str(sheet['A'+str(m)].value)
    jsonValue = line
    try:
        data = json.loads(jsonValue)
        for n in range(0,20):
            Adult = data["ResponseData"]["Outbound"][n]["Adult"]
            GrandTotal = data["ResponseData"]["Outbound"][n]["GrandTotal"]
            airline = data["ResponseData"]["Outbound"][n]["Airline"]
            Arrival = data["ResponseData"]["Outbound"][n]["Arrival"]
            Departure = data["ResponseData"]["Outbound"][n]["Departure"]
            adultFare = data["ResponseData"]["Outbound"][n]["AdultFare"]
            childFare = data["ResponseData"]["Outbound"][n]["ChildFare"]
            FlightClassCode = data["ResponseData"]["Outbound"][n]["FlightClassCode"]
            AgencyCommission = data["ResponseData"]["Outbound"][n]["AgencyCommission"]
            ChildCommission = data["ResponseData"]["Outbound"][n]["ChildCommission"]
            line = ('Line# '+ str(n) + ',' + str(Adult) + ','+ airline +','+ Departure + ',' + Arrival + ',' + FlightClassCode + ','+ \
                str(adultFare) + ','+ str(childFare) +','+ str(AgencyCommission) +','+ str(ChildCommission) + ',' + str(GrandTotal))
            pprint.pprint(line,file)
    except Exception as err:
        print('An exception occurred: ' + str(err))
        continue
file.close()

file1.close()
#pprint.pprint(json.loads(c))
