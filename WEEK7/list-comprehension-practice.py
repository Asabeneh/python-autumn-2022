from countries import countries_data
from pprint import pprint

""" languages = [
    {'name': c['name'], 'languages': c['languages']} for c in countries_data]
pprint(languages)

pprint([[c['name'], c['capital'],c['population'],c['flag']] for c in countries_data])

world_population = sum([c['population'] for c in countries_data])
pprint("{:,}".format(world_population))

 """

def find_country_by_starting_string(start):
    lst =  [c['name'] for c in countries_data if c['name'].lower().startswith(start.lower())]
    return lst

# print(find_country_by_starting_string('f'))
countries_start_with_f = find_country_by_starting_string('f')
countries_start_with_s = find_country_by_starting_string('s')
# pprint(countries_start_with_s)

def filter_countries_starting (start):
    filtered_countries = [c['name'] for c in countries_data if  start.lower() in c['name'].lower() or start.lower() in c['capital'].lower() or start in ', '.join(c['languages']).lower() ]
    return filtered_countries
pprint(filter_countries_starting('nepali'))


