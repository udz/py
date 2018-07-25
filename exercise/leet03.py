'''
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

'''

input = 1994

def intToRoman(num):
    string = str(num)
    list1 = []
    i = 0
    for letter in string:
        list1.append(letter)
    #print(list)
    list1.reverse()
    value = []
    itir = 1
    for i in list1:
        j = int(i)
        if itir == 1:
            if j <= 3:
                value.append('I'*j)
            elif j == 4:
                value.append('IV')
            elif j == 5:
                value.append('V')
            elif j > 5 and j <8:
                value.append('V' + 'I'*(j-5))
            elif j == 9:
                value.append('IX')
        if itir == 2:
            if j > 0 and j <=3:
                value.append('X'*j)
            elif j == 4:
                value.append('XL')
            elif j == 5:
                value.append('L')
            elif j > 5 and j <=8:
                value.append('L' + 'X'*(j-5))
            elif j == 9:
                value.append('XC')
        if itir == 3:
            if j > 0 and j <= 3:
                value.append('C'*j)
            elif j == 4:
                value.append('CD')
            elif j == 5:
                value.append('D')
            elif j > 5 and j <= 8:
                value.append('D' + 'C'*(j-5))
            elif j ==9:
                value.append('CM')
        if itir == 4:
            if j > 0 and j <= 3:
                value.append('M'*j)
            elif j >= 4:
                value.clear()
                value.append('ERROR. Number Out of Bound')
        itir += 1

    value.reverse()
    #print(value)
    string = ''.join(value)
    return string

print('Roman equivalent of',input,'is',intToRoman(input))