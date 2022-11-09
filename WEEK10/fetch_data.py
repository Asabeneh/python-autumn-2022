from fetch_api_data import fetch_api_data
from pprint import pprint

COUNTRIES_API_URL = 'https://restcountries.com/v2/all'
countries  =fetch_api_data(COUNTRIES_API_URL)
 
def find_countries_without_capital(data):
    for c in data:
        if c.get('capital') == None:
            print(c['name'], c.get('capital'), c['population'])
# find_countries_without_capital(countries)
def find_countries_with_land(data):
    for c in data:
        if 'land' in c['name']:
            print(c['name'], c.get('capital'), c['population'])
# find_countries_with_land(countries)


def find_countries_grater_than_100m(data):
    for c in data:
        if c['population'] > 100000000:
            print(c['name'], c.get('capital'), "{:,}".format(c['population']))

# find_countries_grater_than_100m(countries)

lst = [2, 4, 1, 5, 0, 10]

sorted_lst = sorted(countries, key= lambda c:c['population'], reverse=True)
# pprint(sorted_lst[:10])

def find_ten_most_populated_countries(data):
    sorted_lst = sorted(countries, key= lambda c:c['population'], reverse=True)
    ten_countries = sorted_lst[:10]
    return list(map(lambda c:[c['name'], c.get('capital'), c['population']],   ten_countries))

pprint(find_ten_most_populated_countries(countries))
  

CATS_API_URL = 'https://api.thecatapi.com/v1/breeds'
cats = fetch_api_data(CATS_API_URL)
# for cat in cats:
#     print(cat['name'], cat['origin'], cat['weight']['metric'].split(' - '), cat['life_span'].split(' - '))


def find_weights(cats):
    weights = []
    for cat in cats:
        min, max = cat['weight']['metric'].split(' - ')
        average = (int(min) + int(max)) / 2
        weights.append(average)
    return weights

print(find_weights(cats))

average_weight = sum(find_weights(cats)) / len(find_weights(cats))
print(round(average_weight, 2))

