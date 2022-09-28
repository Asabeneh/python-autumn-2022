a = -3
if a > 0:
    print(f'{a} is a positive number')
elif a < 0:
    print(f'{a} is a negative number')
elif a == 0:
    print(f'{a} is a zero')
else:
    print(f'{a} is not a numbeer')

a = -5
if(type(a) == int):
    if a == 0:
        print(f'The absolute value of {a} is {a}')
    elif a < 0:
        print(f'The absolute value of {a} is {a * -1}')
    elif a > 0:
        print(f'The absolute value of {a} is {a}')
    else:
        print('not a number')
else:
    print('Please use an integer')


weather = input('What is weather like today? ').lower()
if weather == 'rainy':
    print('Take your umbrella')
elif weather == 'sunny':
     print('Go out freely')
elif weather == 'cloudy':
    print('There might be rain, consider taking an umbrella')
elif weather =='foggy':
    print('There is limited visibility')
elif weather == 'snowy':
    print('It might be slippery')
else:
    print('No one knows about the weather')