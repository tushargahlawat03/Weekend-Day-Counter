import datetime
year = int(input("Enter year: "))

saturday = 0
sunday = 0

start_date = datetime.date(year, 1, 1)
end_date = datetime.date(year, 12, 31)

total_days = (end_date - start_date).days + 1

for i in range(total_days):
    a = start_date + datetime.timedelta(days=i)

    if a.weekday() == 5:      
        saturday += 1
    elif a.weekday() == 6:    
        sunday += 1

print("Saturday:", saturday)
print("Sunday:", sunday)
print("Total weekends:", saturday + sunday)
