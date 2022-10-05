# Data: Number, Strings, Booleans(True or False), List, tuples, set, dictionary


# TUPLES

# to create an empty tuple
tpl = tuple() # or ()
print(tpl)
nums_tpl = (1, 2,5, 2, 3, 4, 5, 5)
print(nums_tpl)
print(len(nums_tpl))
print(nums_tpl.count(2))
print(nums_tpl.count(5))
print(nums_tpl.index(3))

print('Using for loop in tuples')
for n in nums_tpl:
    print(n)

print('Using while loop in tuples')
i = 0
while i < len(nums_tpl):
    print(nums_tpl[i])
    i = i  + 1