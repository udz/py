import csv

file = open('CSV/test.csv')

exampleReader = csv.reader(file)


for row in exampleReader:
    print('Row #' + str(exampleReader.line_num) + ' ' + str(row) )

#exampleData = list(exampleReader)
#print(exampleData)

file.close()