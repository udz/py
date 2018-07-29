# Program to check if the DOB is at least before 16 years old
import datetime

delta = datetime.timedelta(days=365*16)
input = datetime.datetime(2001,7,22)
current = datetime.datetime.now()

if input < current - delta:
    print('DOB is Valid')
else:
    print('Invalid DOB')
