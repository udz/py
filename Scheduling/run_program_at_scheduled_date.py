# Pausing until a specific date

import datetime
import time

# Execute function after set date time
new_year = datetime.datetime(2018,7,28,17,39,0)
while datetime.datetime.now() < new_year:
    time.sleep(1)
print('Executed rest of the program')

# Format datetime to readable format 
print(new_year.strftime('%j %w %A %a %I:%M:%S %p'))
print(datetime.datetime.now().strftime('Today is %d of %B,%Y'))

# String to datetime
sample_date = 'October 15,2018'
dt = datetime.datetime.strptime(sample_date,'%B %d,%Y')
print(dt)
