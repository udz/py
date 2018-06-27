'''
Primer on lambda function
detail on following link https://stackoverflow.com/questions/18296755/python-max-function-using-key-and-lambda-expression

'''

lis = ['1','2','555','1010','66',20.2,3.4]

#print(max(lis)) # strings are compared lexicographically. This gives error in python 3 when list contains different data types 
maximum = max(lis, key=lambda x:int(x)) #compare `int` version of each item
print(maximum)

print('\n')
# Example 2: Applying max to a list of lists.

list1 = [(1,'a'),('28','c'), (4,'e'), (-1,'z')]
#print(max(list1))  # this gives error in Python 3 when type of keys are different

# if you want to compare each item by the key at index 0
maximum = max(list1, key = lambda x: int(x[0]))
print(maximum)
# if you wanted to compare each item by the value at index 1
maximum = max(list1, key = lambda x: x[1])  
print(maximum)