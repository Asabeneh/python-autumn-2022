""" import custom_modules
print(custom_modules.add_two_nums(99, 1))
print(custom_modules.make_square(3))
print(custom_modules.add_all_nums(50))
print(custom_modules.generate_evens(20))
print(custom_modules.generate_evens(31, 9)) """

""" from custom_modules import add_all_nums, add_two_nums, make_square, generate_evens

print(add_two_nums(99, 1))
print(make_square(3))
print(add_all_nums(50))
print(generate_evens(20))
print(generate_evens(31, 9))  """


import sys
sys.path.insert(0, 'WEEK7/my_modules' )
from custom_modules import add_all_nums, add_two_nums, make_square, generate_evens



print(add_two_nums(99, 1))
print(make_square(3))
print(add_all_nums(50))
print(generate_evens(20))
print(generate_evens(31, 9))



""" from custom_modules import *
print(add_two_nums(99, 1))
print(make_square(3))
print(add_all_nums(50))
print(generate_evens(20))
print(generate_evens(31, 9))  """