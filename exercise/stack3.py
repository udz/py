
original_list = ['d','b','c','a','b','c',1,3]
unique_list = []

for value in original_list:
    if value not in unique_list:
        unique_list.append(value)
        
print(unique_list)