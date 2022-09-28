# what are loops? 

# for loop

# [1, 2, 3, 4]



print(list(range(100, 1001, 100)))

for item in [0, 1, 2, 3, 4, 5]:
    print(item)

lst = []
for country in ['Finland','Sweden','Norway','Denmark','Iceland']:
    lst.append([country, country.upper(), len(country), country.upper()[0:3]])

print(lst)

total = 0
for i in range(1, 6): # [1, 2, 3, 4, 5]
    total = total + i
    print(i, total)
print(total)

print(sum(range(1, 6)))

countries = ['Finland','Sweden','Norway','Denmark','Iceland']

countries_with_land = []
countries_without_land = []
for country in countries:
    if 'land' in country:
        countries_with_land.append(country)
    else:
        countries_without_land.append(country)

print(countries_with_land)
print(countries_without_land)

names = ['Tuomas', 'Marika', 'Marja', 'Bibek', 'Mikko', 'Laura', 'Ivan', 'Fuad','Phuong','Swapna','Arun','Alfonso','Marjukka','Asabeneh','Fabian']

print(len(names))

short_names = []
long_names = []

for name in names:
    if len(name) <= 6:
        short_names.append(name)
    else:
        long_names.append(name)
print(short_names)
print(long_names)

nums = [2, 3, 0, -5, 6, 7,-8, 1]

print('This is for loop with break')
for n in nums:
    if n < 0:
        break
    print(n)

print('This is the for loop with continue')
positives = []
for n in nums:
    if n < 0:
        continue
    positives.append(n)
    print(n)
print(positives)

# While Loop

print('This a while loop')
# 0 => 5
count = 0
while count < 6:
    print(count)
    count = count + 1


count = 5
while count >= 0:
    print(count)
    count = count - 1
  
students = []
while True:
    name = input('Enter name: ')
    if name == 'end' or name == 'quite' or name == '0':
        break
    students.append(name)
print(students)
