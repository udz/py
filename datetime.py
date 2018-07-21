import datetime

today = datetime.datetime.today()
print("Today: ",today)
yesterday = today - datetime.timedelta(days=1)
print("Yesterday: ",yesterday)
tomorrow = today + datetime.timedelta(days=1)
print("Tomorrow: ",tomorrow)

print("Time between yesterday and tomorrow is ",tomorrow - yesterday)

dt = datetime.datetime.strptime("2016-04-15T08:27:18-0500", "%Y-%m-%dT%H:%M:%S%z")
print(repr(dt))
print(dt.tzname())

date = datetime.date(2018,7,30)
print(date,"  ",date.year,date.month, date.day)

noon = datetime.time(12,30,10)
print(noon, " ", noon.hour,noon.minute,noon.second)

from datetime import datetime, timedelta, timezone

NST = timezone(timedelta(hours=+6.5))
dtn = datetime(2015, 1, 1, 12, 0, 0, tzinfo=NST)
print(dtn)
dtn = datetime(2015, 1, 1, 12, 0, 0, tzinfo=timezone(timedelta(hours=9), 'JST')) 
print(dtn.tzname())

def get_n_days_after(date_format="%d %B %Y",add_days = 120):
    date_n_days_after = datetime.now() + timedelta(days=add_days)
    return date_n_days_after.strftime(date_format)

print(get_n_days_after())

# Convert POSIX timestamp to utc date
import time

seconds_since_epoch = time.time()
print(seconds_since_epoch)
utc_date = datetime.utcfromtimestamp(seconds_since_epoch)
print(utc_date)

local_date = datetime.fromtimestamp(seconds_since_epoch).strftime('%Y-%m-%d %H:%M:%S')
print(local_date)