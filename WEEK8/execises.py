""" Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
 """

""" lst = []
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
for item in list_of_lists:
    lst.extend(item[0])

print(lst) """

from countries import countries_data
from pprint import pprint
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flat_list = [n for item in list_of_lists for n in item[0]]
print(flat_list)

# pprint(countries_data)
countries_name = [country['name'] for country in countries_data]
pprint(countries_name)
capitals = [country['capital'] for country in countries_data]
pprint(capitals)
populations = [country['population'] for country in countries_data]
pprint(populations)

world_population = sum(populations)
print(world_population)
print("{:,}".format(world_population))