# sum1-100.py
print('summation of 1 - 100 using for loop')
sum = 0
for i in range(101):
    sum += i
print(sum)    

print('summation of 1 - 100 using while loop')
j = 100
sum = 0
while j >= 1:
    sum += j
    j-=1
print(sum)


# range(start,stop,step)
print('count up step 2')
for i in range(12, 20,2):
    print(i)


print('counting down')
for i in range(5, -1, -1):
    print(i)
