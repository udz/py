
# Add numbers upto a certain digit

count = input('Enter upto which number should the program add: ')

max = int(count)
sum = 0
for i in range(0,max+1):
    sum += i

print(sum)
