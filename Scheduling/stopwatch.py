import time
import msvcrt

time1 = time.time()
startTime = time1
time2 = 0
count = 0

print('*** Press Space to Log Lap, Press Enter to End The Program ***')

while True:
    if msvcrt.kbhit():
        key = msvcrt.getch()
        time2 = time.time()
        if key==b' ' or key ==b'\r':
            count += 1            
            diff = time2 - time1
            print('Lap',count,'-',round(diff,2),'seconds')
            time1 = time2
        if key ==b'\r':
            print('Total Time Elapsed:',round(startTime - time2,2),'seconds')
            break
