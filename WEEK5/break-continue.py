# break: stops the loop
# contiue: allow as to skip an item in the iteration

for i in [1, 2, 3, 4, 5]:
    if i == 3:
        break
    print(i)


names = ['Tuomas', 'Marika', 'Marja', 'Bibek', 'Mikko', 'Laura', 'Ivan', 'Fuad','Phuong','Swapna','Arun','Alfonso','Marjukka','Asabeneh','Fabian']

for name in names:
    if name == 'Bibek':
        break
    print(name)

print('Skip all the long names')
for name in names:
    if len(name) > 6:
        break
    print(name)


nums = [1, 2, 3, 4, 5]
print(len(nums))
print(len('Finland'))