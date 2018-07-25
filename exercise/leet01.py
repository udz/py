'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''

nums = [3,2,11,15,7]
target = 9

i=0
j=0
temp = 0
for i in range(len(nums)):
    for j in range(len(nums)):
        if j <= i:
            continue
        temp = nums[i]+nums[j]
        #print(temp)
        if target == temp:
            print('num[',i,']+num[',j,']=',target)
            break
    if target == temp:
        break
if target != temp:
    print('Not Matched')
