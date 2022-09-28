# strings
# What are strings?
# Strings are data types. Any text data form we call it a string data type.
# Any text under single or double quote is a string
# A string could be a single character or many pages of text.
# A number with in a single or double quote is also a string

from itertools import count


print('Hello World!')
print(type('Hello World!'))

letter = 'a'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
vowels = 'aeiou'
print(type(letter))
print(lowercase_letters)
print(type(lowercase_letters))
print(len(lowercase_letters))
print(len(vowels))
print(lowercase_letters.upper())

uppercase_letters = lowercase_letters.upper()
print(uppercase_letters)

sent = '   I love finland    '
para = 'I love Finland. Because the people is nice and the country is beautiful.'
print(sent)
print(sent.upper())
print(sent.lower())
print(sent.title())
print(sent.split())
print(para.split('. '))
print(sent.replace('finland', 'Sweden'))
print(sent)
print(sent.strip())

txt = 'I love# people. #Peo#ple are goo#d.'
print(txt)
print(txt.replace('#',''))

country = 'Finland'
print(len(country))
print(country[0])
print(country[1])
print(country[2])
print(country[3])
print(country[4])
print(country[5])

last_index = len(country) - 1
print(country[last_index])
print(country[6])
print(country[-1])
print(country[-2])
print(country[0:3])
print(country[:3])
print(country[-7:-4])
print(country[3:7])
print(country[3:])
print(country[2:4])
print(country[-4:])

# print(type(country))
# print(country.split())
# print(list(country))
# print(list(lowercase_letters))

# methods of strings
print(country.find('F'))
print(country.find('d'))
print(country.find('land'))
print(country.startswith('F'))
print(country.startswith('f'))
print(country.startswith('S'))
print(country.endswith('d'))
print(country.endswith('land'))


""" txt = 'Everybody is looking for love. There is not thing like love in this world. Love is somehting great.'
print(txt.lower().count('is'))
print(len(txt))
print(txt.lower().rfind('love')) """

print('I love Pyton.\nI love JavaScript too.\nI love programming languages')

print('Helllo' + ' ' +  'World!')

first_name = 'Asabeneh'
last_name = 'Yetayeh'
job = 'Programmer'
age = 250
country = 'Finland'
city = 'Helsinki'

full_name = first_name + ' ' +  last_name
print(full_name)

print("I am " + full_name + '. ' + 'I am a ' + job + ' and I live in ' + city + '. ' + ' I am ' + str(age) + ' years old.')

""" 
I am Asabeneh Yetayeh. I am a progammer and live Helsinki, Finland. I am 250 years old.
 """
print("I am {}. I am a {} and live {}, {}. I am {} years old.".format(full_name, job, city, country, age))

print(f"I am {full_name}. I am a {job} and live {city}, {country}. I am {age} years old.")

a = 3
b = 4
""" 
3 + 4 = 7
 """
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} x {b} = {a * b}")
print(f"{a} / {b} = {a / b}")