# Nested Dictionary Demo
import pprint

allGuests = {'Ujjwal':{'apple':5,'orange':10,'momo':10},
          'Rajeev':{'momo':2,'Samosa':10,'paneer matar':3},
          'Roshan':{'orange':4,'apple':2}}

def totalBrought(guests,item):
    count = 0
    for k,v in guests.items():
        count = count + v.get(item,0)
    return count

print('Total items brought ')
print('Apples = ' + str(totalBrought(allGuests,'apple')))
print('Ornage = ' + str(totalBrought(allGuests,'orange')))
print('momo = ' + str(totalBrought(allGuests,'momo')))
print('Samosa = ' + str(totalBrought(allGuests,'Samosa')))
print('Paneer Matar = ' + str(totalBrought(allGuests,'paneer matar')))

pprint.pprint(allGuests)
