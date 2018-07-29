import datetime
import time

dt = datetime.datetime.now()
print('Date:',dt.year,dt.month,dt.day)
print('Time:',dt.hour,dt.minute,dt.second)
print(dt)

dt = datetime.datetime.fromtimestamp(time.time())
print(dt)

delta = datetime.timedelta(weeks = 2, days=10,hours=5, minutes=12,seconds=50,milliseconds=100)
newdate = dt + delta
print(delta)
print(newdate)
