# 
empty_dict = {}
print(empty_dict)
print(len(empty_dict))

""" list() # []
tuple() # ()
set()
dict() # {} """

fin_to_eng = {
'talo':'house',
'kirja':'book',
'kirjasto':'library',
'auto':'car',
'kissa':'cat',
}

print(fin_to_eng)
print(len(fin_to_eng))
fin_to_eng['koulu'] = 'school'
fin_to_eng['opeskelija'] = 'student'
fin_to_eng['bussi'] = 'buss'
print(fin_to_eng)

print(fin_to_eng['talo'])
print(fin_to_eng['auto'])
print(fin_to_eng['bussi'])

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'country':'Finland',
    'city':'Helsink',
    'age':250,
    'is_married':True,
    'skills':['HTML','CSS','JavaScript','TypeScript','React','Redux','Python'],
    'address':{
        'street_name':'Space street',
        'zipcode':'02770',
        'email':'asab@gmail.com',
        'tel':'045454545'
    },
    'schools':['Metropolia','Helsinki','Wageningen']

}
print(person)
print(person['first_name'])
print(person['last_name'])
person['nationality'] = 'Ethiopian'
person['age'] = 39
print(len(person))
print(person['nationality'])
print(person)

# How many skills does this person have?


skills = person['skills']
print(skills)
print(len(skills))

# Home work
# Asabeneh Yetayeh has 7 skills. These are HTML, CSS, JavaScript, TypeScript, React, Redux and Python.
# print(person['school'])


if person.get('schools'):
    print(person['schools'])

if person.get('hobbies'):
    print( person['hobbies'])
else:
    person['hobbies'] = 'Hikking'
  

print(person)


keys = person.keys()
print(list(keys))
values = person.values()
print(values)





""" print(tpl[0])
print(tpl[1])
print(tpl[2])
  """
first_p, second_p, third_p =('Bibek','Fabian','Arun')
print(first_p)
print(second_p)
print(third_p)

items = person.items()
print(items)
for item in items:
    k,v = item
    print(v)

# Truthy and False values
# Truthy values: all strings, all numbers except zero, True
# Falsy value: 0, False, None, empty values
if '':
    print('value')
person.pop('first_name')


print(person)
p2 = person

p2['job'] = 'programmer'
print(p2)
print(person)
