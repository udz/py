import datetime
# The size of each step in days 
day_delta = datetime.timedelta(days=1)
start_date = datetime.date.today()
end_date = start_date + 7*day_delta
for i in range((end_date - start_date).days):
    print(start_date + i*day_delta)
