# map, filter, reduce
from countries import countries_data
from pprint import pprint
# map is one to one match of a data value
# [1, 2, 3, 4] = [2, 4, 6, 8] or [1, 4, 9, 16]
# ["apple", "banana"] = ["orange", "Guava"]

nums = [1, 2, 3, 4]
""" lst =  [n**2 for n in nums]
print(lst) """



lst = map(lambda x: x * 2, nums)
print(list(lst))
# pprint(countries_data)
data = map(lambda x:[x['name'],x['capital'], x['population']], countries_data)
pprint(list(data))

countries=['Finland','Sweden','Norway', 'Denmark','Iceland']
lst = map(lambda country:[country.upper(), country.upper()[:3] ], countries)
print(list(lst))


# Filter

# [0, 1, 2, 3, 4, 5] => [0, 2, 4] or [1, 3, 5]
nums = [0, 1, 2, 3, 4, 5] 
print([n for n in nums if n % 2 == 0])
evens = filter(lambda n: n % 2 == 0, nums)
print(list(evens))
odds = filter(lambda n : n % 2 != 0, nums)
print(list(odds))


def is_land(c):
    return 'land' in c['name']
countries_with_land = filter(is_land, countries_data)
filtered_countries = list(countries_with_land)
pprint(list(map(lambda c:c['name'], filtered_countries)))


# reduce
from functools import reduce

nums = [1, 2, 3, 4, 5] 
total = reduce( lambda a,b: a + b, nums)
print(total)
