'''
Using the Python language, have the function SimpleSymbols(str) take the str 
parameter being passed and determine if it is an acceptable sequence by either 
returning the string true or false. The str parameter will be composed of 
+ and = symbols with several letters between them (ie. ++d+===+c++==a) and 
for the string to be true each letter must be surrounded by a + symbol. 
So the string to the left would be false. The string will not be empty and 
will have at least one letter. 

Sample Test Cases
Input:"+d+=3=+s+"
Output:"true"

Input:"f++d+"
Output:"false"
'''

string = '+f++d+d+'

def SimpleSymbols(str):
    output = True
    position = 0
    for char in str:
        if char.isalpha():
            if position == 0 or position == (len(str)-1):
                output = False
            elif str[position-1] == '+' and str[position+1] == '+':
                pass
            else:
                output = False
        position += 1
    return output

print(SimpleSymbols(string))