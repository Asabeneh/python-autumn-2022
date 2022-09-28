def make_square (n):
    return n * n

print(make_square(3))
print(make_square(10))
print(make_square(-9))

countries = ['Finland','Sweden','Norway','Denmark','Iceland']
vegatables = ['Kale','Onino','Potato','Beet root','Carrot']
fruits = ['Apple','Banana','Orange','Papaya','Mango','Avocado']

names = ['Tuomas', 'Marika', 'Marja', 'Bibek', 'Mikko', 'Laura', 'Ivan', 'Fuad','Phuong','Swapna','Arun','Alfonso','Marjukka','Asabeneh','Fabian']

def change_list_to_uppercase(lst):
    uppercase_names = []
    for name in lst:
        uppercase_names.append(name.upper())
    return uppercase_names

print(change_list_to_uppercase(names))
print(change_list_to_uppercase(countries))
print(change_list_to_uppercase(vegatables))
print(change_list_to_uppercase(fruits))

nums = [1, 2, 3, 4, 5, 6]
def double_num(n):
    return n * 2


def list_of_evens(lst):
    evens = []
    for i in lst:
        evens.append(double_num(i))
    return evens

print(list_of_evens(nums))



