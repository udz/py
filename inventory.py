import pprint

inventory = {'rope':2,
             'torch':5,
             'knife':2,
             'bullets':10,
             'pistol':1,
             }

def displayInventory(inv):
    totalItems = 0
    for k,v in inv.items():
        print(str(k) +':'+ str(v))
        totalItems += v
    print('Total number of items are ' + str(totalItems))

displayInventory(inventory)

dragonLoot = ['gold coin','bullets','bullets','gold coin','ruby']
print("You've discovered a Dragon Loot!")

def addToInventory(inv, addedItems):
    for item in addedItems:
        if item in inv:
            inv[item] += 1
        else:
            inv[item]=1
    print('--The items has been added to your inventory--')

addToInventory(inventory,dragonLoot)

displayInventory(inventory)
