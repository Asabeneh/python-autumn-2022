# In this file we will learn about builtin functions

'''
- Builting Functions
    - print(), len(), sum(), max(), min(), input(), round(), abs(), dir(),str(), int(), range(), type(), help()


'''
# print may or may not have an input
# Print can take unlimited number of inputs(arguments)
from itertools import count


print()

# print with only one input
print('Hello world')

# print with three inputs(arguments)
print('Hello', 'Asabeneh', 2022)
print()
print('I love Python.\nBut I prfer JavaScript')
print('******-----***======****')

# Lenght of a string
# String is any data inside a single or double quote

print('Asabeneh')
print("Asabeneh")
print("""Asabeneh""")

print(len('Asab'))
print(len('Finland'))
print(len('Hello World!'))

# list data type
nums = [1, 2, 3, 4, 5]
print('There are', len(nums), 'numbers')
print('The length of the phone is', len('123-567-8234'))
names = ['Asab','John','Donland','Elon']
print('There are ', len(names), 'names')

# min

print('The minimum value is', min(9, 4, -2, 1, 0, -1 ))
print('The maximum value is', max(9, 4, -2, 1, 0, -1 ))
print(sum([9, 4, -2, 1, 0, -1]))



print(round(9.81))
print(round(9.81567, 2))
print(round(3.14))
print(round(3.14, 1))
print(round(2.77))
print(round(2.77, 1))

# abs
print(abs(-5))
print(abs(7))
# print(dir(names))
# print(dir('text'))
# print(dir(1))

# Integers: ... -3, -2, -1, 0, 1, 2, 3...
# Floats      -0.2,  -0.1, 0, 0.1, 0.2 ...
# complex  1 + j, 2 +2j
print(type(1))
print(type(10))
print(type(0))
print(type(-1))

print(type(2.77))
print(type(9.81))
print(1 + 1j)
print(type(1 + 1j))

# strings data type
print(type('Asab'))
print(type('Finland'))
print(type('Helsinki'))


# print(help('string'))
countries = ['Finland','Sweden','Estonia','Denmark','Norway', 'Finland']
print(dir(countries))
countries.append('Iceland')
countries.append('Russia')
print(countries)
print(countries.count('Finland'))
countries.extend(['Germany','Belgium','France','The Netherlands'])

print(countries)
print(countries.index('Finland'))

print('1' + str(2))
print(int('1') + 2)

print(type(True))
print(type(False))
# int() and str()
print('1')
print(type('1'))
print(type(int('1')))
# print('1' + 1)
print(int('1') + 1)
print('1' + str(2))

""" # range(start, stop, step)

# Whole numbers
print('=== Whole Numbers ===')
print(list(range(0, 101)))
# Natural Numbers
print(' === Natural Numbers or Counting Numbers ===')
print(list(range(1, 101)))

print('==== Integers ====')
print(list(range(-100, 101)))

print('=== Even numbers ===')
print(list(range(0, 101, 2)))

print('=== Odd numbers ===')
print(list(range(1, 101, 2)))
print(list('Asabeneh'))
print(list('Finland')) """

# input
# Input allows to get data from a user
first_name = input('Enter your name: ')
country = input('Where are you from? ')
year = input('When were you born? ')

age = 2022 - int(year)
print('Welcome', first_name)
print('That is great, you are from ', country)
print('You are ', age, 'years old.')


