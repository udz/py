# Function to print list items

fruits = ['apple','banana','orange']
integers = [11,22,33,44,55]

def listOut(list1):
    fullList =''
    for i in range(len(list1)-1):
        fullList += str(list1[i]) + ', '
    fullList += 'and '+ str(list1[len(list1)-1])
    return(fullList)
    
print(listOut(fruits))
print(listOut(integers))
