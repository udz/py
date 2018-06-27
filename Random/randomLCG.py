# Theory with conditions https://www.cse.wustl.edu/~jain/iucee/ftp/k_26rng.pdf
# Below code was taken from the following link http://people.duke.edu/~ccc14/sta-663-2016/15A_RandomNumbers.html
# List of big prime numbers http://compoasso.free.fr/primelistweb/page/prime/liste_online_en.php

#def rng(m=2**32, a=1103515245, c=12345):
# def rng(m=10163, a=9967, c=342):  # This one works

# Generates non repeating numbers
# def rng(m=9967, a=9623, c=234): # for 4 digits 
# def rng(m=99877, a=99089, c=234): # for 5 digits
# def rng(m=999863, a=999377, c=234): # for 6 digits
# def rng(m=9999889, a=9990499, c=234): # for 7 digits

# 7015678486M
"""
condition m > a
both m and a are relatively big prime numbers
m should be closest prime number to the number of digits you'd want
value of c should be used to make the sequence unpredictable, however, same value of c should be used for the entire range
"""
def rng(m=9967, a=9623, c=234):
    rng.current = (a*rng.current + c) % m
    return rng.current

#for i in range(9967):
#    print(rng())
    
# setting the seed
rng.current = 3

file = open('Random/test_4_digits.csv','w')
for i in range(9967):
    file.write(str(rng()))
    file.write('\n')
file.close()



