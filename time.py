import time

print(time.time())

def calcProd(n):
    product = 1
    for i in range(1,n):
        product = product * i
    return(product)

startTime = time.time()
prod = calcProd(100000)
endTime = time.time()

print('The length of product is: ' + str(len(str(prod))))
time.sleep(2)
print('It took %s seconds to process' %(endTime - startTime))
