import time, sys

def timekeeper():
    start = time.time()
    while 1:
        try:
            c = sys.stdin.read(1)
        except IOError: break
    end = time.time()
    timeElapsed = end - start
    return(timeElapsed)

print(timekeeper())