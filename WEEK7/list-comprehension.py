""" nums = [1, 2, 3, 4, 5] # [2, 4, 6, 8, 10]

new_nums = []
for i in nums:
    new_nums.append(i * 2)
print(new_nums)

skills = ['HTML','CSS','JavaScript','TypeScript','React','Redux','Python']
new_skills = []
for skill in skills:
    new_skills.append(skill.upper())

print(new_skills)

evens = []
for num in nums:
    if num % 2 == 0:
        evens.append(num)
print(evens)

countries = ['Finland','Sweden','Norway','Denmark','Iceland']
lst = []
for country in countries:
    lst.append([country, country.upper(), country.upper()[:3], len(country)])
print(lst)

 """
from pprint import pprint

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
new_nums = [i * 2 for i in nums]
print(new_nums)
skills = ['HTML','CSS','JavaScript','TypeScript','React','Redux','Python']
new_skills = [skill.upper() for skill in skills]
print(new_skills)
evens = [ num for num in nums if num % 2 == 0]
print(evens)

countries = ['Finland','Sweden','Norway','Denmark','Iceland']


lst = [[c, c.upper(), c.upper()[:3], len(c)] for c in countries]
pprint(lst)

countries_with_land = [c for c in countries if 'land' in c]
print(countries_with_land)

odds = [n for n in nums if n % 2 != 0]
print(odds)

