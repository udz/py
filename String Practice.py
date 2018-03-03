str = 'Helo World'.rjust(30,'*')
print(str)

tableData = [['apples','oranges','cherries','bananas'],
             ['Alice','Bob','Carol','David'],
             ['dogs','cats','moose','goose']]


for table in tableData:
    #print(maximum)
    for record in table:
        str = record.rjust(len(record))
        print(str)
