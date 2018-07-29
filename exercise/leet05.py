''' 
Given an array nums of n integers, are there elements a, b, c in nums such that 
a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

The solution set must not contain duplicate triplets.
'''
nums = [-1, 0, 1, 2, -1, -4]
solution = []
count = 0
for i in range(len(nums)-2):
    for j in range(i+1,len(nums)-1):
        for k in range(j+1,len(nums)):
            if nums[i] + nums[j] + nums[k] == 0:
                solution.append([nums[i],nums[j],nums[k]])
                count += 1
print(solution)
print('There are',count,'triplets for which sum is 0')