
# zip function
a = [1,2,3]
b = [4,5,6]

zipped = zip(a,b)
print(type(zipped))

for item in zipped:
    print(item)


print(sum(a))