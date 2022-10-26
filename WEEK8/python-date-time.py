from datetime import datetime, date as date_module, time

current_time = datetime.now()
date = current_time.day
month = current_time.month
year = current_time.year 
hours = current_time.hour
minutes = current_time.minute
weekday = current_time.weekday()
week_days = ['Monday','Tuesday','Wendesday','Thursday','Friday','Saturday','Sunday']
day = week_days[weekday]
print(day)

# European Time Format

print(f'{date}-{month}-{year}')
print(f'{date}/{month}/{year}')
print(f'{day}, {date}-{month}-{year} {hours}:{minutes}')

# American


print(f'{month}-{date}-{year}')
print(f'{month}/{date}/{year}')
print(f'{day}, {month}-{date}-{year} {hours}:{minutes}')

new_year = datetime(2023, 1, 1)
print(new_year.year)

t = current_time.strftime("%H:%M:%S")
print(t)
print( current_time.strftime('%a'))
print( current_time.strftime('%A'))
print(current_time.strftime('%w')) # Sun Mon Tus Wen
print(current_time.strftime('%d'))

date_string = "5 December, 2019"
date_obj = datetime.strptime( "5 December, 2019", "%d %B, %Y")
print(date_obj.year)


d = date_module(2023, 1, 1)
today = date_module(2022, 10, 26)
remaining_days = d - today
print(remaining_days)

