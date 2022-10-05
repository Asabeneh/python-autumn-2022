from countries import countries_data
from pprint import pprint

languages = []
for country in countries_data:
    languages.extend(country['languages'])

print(languages)
print(len(languages))
print(len(set(languages)))



