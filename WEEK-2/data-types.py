# In this file, we will learn about data types
""" - Data Types
    - Numbers(Int, float, Complex)
    - Booleans(True and False)
    - Strings
    - List
    - Set
    - Tupes
    - Dictionary """

# Numbers(int, float, complex)
gravity = 9.81
boiling_temp = 100
pi = 3.14
print(type(2))
print(type(9.81))
print(type(1 + 4j))

# Booleans( True or false)
isRaing = True
isMarried = False
print(type(True))
print(type(False))
print(type(4 > 5))
print(type(len('cat') == len('dog')))
print('cat' == 'dog')
print(len('cat') == len('dog'))
print(len('dragon') == len('python'))
print('on' in 'dragon')
print('gon' in 'Python')

# Strings
# Any data type udner single or double quotes are strings
letter = 'a'
letters = 'abcdefghijklmnopqrstuvwxyz'
vowels = 'aeiou'
first_name = 'Asab'
country = 'Finland'
senetence = 'I love python becuase it is very easy to learn and use'
print(type(letter))
print(len(letter))
print(len(letters))
print(len(vowels))
zipcode = '02770'
phone_number = '1234-234-567'

# List data type, list is a mutable data type and it is also order
nums = [1, 2, 3, 4, 5]
crazy_list = [1, 2, False, 'Asab',('COVID', 2019),['Asab','Finland'],  {'name':'Asab'}]
print(len(nums))
print(sum(nums))



# Tuple, it is an order data and immutable

tpl = (1, 2, 3, 4, 5)
skils = ('HTML','CSS','JS','Python')
hobbies = ['']

# Set, is a unique data elements

st = {1, 2, 3, 4, 4, 5}
print(st)
print(len(st))

# Dictionary
# It is a data structure based on key and value pair

finnish_to_eng = {
    'kirja':'book',
    'talo':'house',
    'Kauppa':'shop',
    'peruna':'potato',
    'kiitos':'Thanks'

}
print(finnish_to_eng)
print(len(finnish_to_eng))

# 3 x 4
arr = [
    [1, 2, 3, 4],
    [2, 3, 4, 5],
    [6, 7, 8, 9]
]
print(arr)