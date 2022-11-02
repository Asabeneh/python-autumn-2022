
a = 5
""" if type(a) == int:
    if a > 0:
        print(f'{a} is a positive number')
    elif a == 0:
        print(f'{a} is zero')
    elif a < 0:
        print(f'{a} is a negative number')
    else:
        print(f'{a} is an unknown value')
else:
    print('The value is not a number') """

""" try:
    if a > 0:
        print(f'{a} is a positive number')
    elif a == 0:
        print(f'{a} is zero')
    elif a < 0:
        print(f'{a} is a negative number')
    else:
        print(f'{a} is an unknown value')
except:
     print('The value is not a number')
finally:
    print('I am a final block and I run all the time at the end of the excution') """


""" try:
    print(age)
except TypeError:
    print('There is a type Error')
except NameError:
    print('There is name error')
except ZeroDivisionError:
    print('It is not allowed to divide a number by 0')
 """
    

try:
    print(age)
except Exception as e:
    print(e)
