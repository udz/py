import threading, time

print('Start of the Program')

def takeANap():
    time.sleep(5)
    print('Wake Up')

threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('End of the Program')