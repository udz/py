# Multithreading with arguments
import threading

#def printf(var1,var2,var3,separator):
#    print(var1,var2,var3,sep=separator)

def printf(*argv,separator):
    var = argv[0]
    for i in range(1,len(argv)):
        var = var + separator + argv[i]
    print(var)

threadObj = threading.Thread(target=printf,args=['apple','orange','banana','grape'],kwargs={'separator':' & '})
threadObj.start()
