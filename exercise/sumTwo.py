'''
Source: https://leetcode.com/problemset/all/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''

def sum_two(numbers, sum):
    for i in range(len(numbers) - 1):
        a = numbers[i]
        print('a = ' + str(a))
        for j in range(i+1,len(numbers)-1,1):
            b = numbers[j]
            print('b = '+ str(b))
            if (a + b) == sum:
                return([a,b])
    return(False)

integers = [2,3,4,5,77,34]
target_sum = 9

print(sum_two(integers,target_sum))
