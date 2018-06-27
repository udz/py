# LCG
'''
def lcg(modulus, a, c, seed):
    while True:
        seed = (a * seed + c) % modulus
        yield seed
'''

#print(str(lcg(32,1664525,1013904223,343)))


def seedLCG(initVal):
    global rand
    rand = initVal

def lcg():
    a = 1140671485
    c = 128201163
    m = 2**24
    global rand
    rand = (a*rand + c) % m
    if len(str(rand))<8:
        diff = 8 - len(str(rand))
        return(diff*"0"+str(rand))
    return str(rand)

seedLCG(1)

file = open('Random/test.csv','w')
for i in range(10000000):
    #print(lcg())
    file.write(lcg())
    file.write('\n')
file.close()
"""
def lcg():
a = 1140671485
c = 128201163
m = 2**24
global rand
rand = (a*rand + c) % m
return rand / m
"""