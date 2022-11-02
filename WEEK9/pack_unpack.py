nums = [2019, 2020, 2021, 2022]
covid_19, second_year, third_year, current_year = nums
print(covid_19)
print(current_year)

tpl = ('Asabeneh', 250, 'Finland')

first_name, age, country = tpl

print(first_name, age, country)

skills = ['HTML', 'CSS', 'Sass', 'JS', 'React', 'Redux', 'Node', 'MongoDB', 'MYSQL']
a, b, c, d, *js_libraries,e, f, g = skills
print(a, b, c, d, js_libraries, e, f)

def add_nums(a, b, c, d, e):
    return a + b + c + d + e

nums = [1, 2, 3, 4, 5]

print(add_nums(3, 4, 5, 2, 3))
print(add_nums(*nums))

args = [10, 110, 10]

print(list(range(*args)))

def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'



dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}

print(unpacking_person_info(**dct)) # Asabeneh lives in Finland, Helsinki. He is 250 years old.

def sum_all_nums(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(sum_all_nums(1, 3, 4, 2, 10))


def packing_person_info(**kwargs):
    for key in kwargs:
        print(key, kwargs[key])

print(packing_person_info(name="Asabeneh",
      country="Finland", city="Helsinki", age=250))


lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
print(lst_one + lst_two)

lst = [0, *lst_one, *lst_two, 8, 9, 10]
print(lst)

countries = ['Finland','Sweden','Norway','Denmark','Iceland']

for i, v in enumerate(countries):
    print(f'{i + 1} - {v}')



fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']

print(list(zip(fruits, vegetables)))

for f,v in zip(fruits, vegetables):
    print(f, v)
