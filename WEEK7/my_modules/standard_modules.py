# import math
# from math import pi, sqrt, floor, ceil, factorial, pow
from math import *
import random

def calculate_area (r):
    pi = 3.14
    area = pi * r * r
    return round(area, 2)


print(calculate_area(10))
print(calculate_area(20))

print(sqrt(4))
print(sqrt(2))
print(floor(3.14))
print(ceil(3.14))
print(factorial(5)) # 5 * 4 * 3 * 2 * 1
print(dir(random))
print(random.randint(5, 25))
