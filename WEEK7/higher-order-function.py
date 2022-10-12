# Higher order function is a function that takes other function as a parameter
# Higher order function a function that return other function as a return value



def make_square(n):
    return n ** 2

def make_cube(fn, n):
    return fn(n) * n

print(make_cube(make_square, 2))
print(make_cube(make_square, 3))


def do_math(a, b):
    def add_two_nums():
        return a + b
    def multiply():
        return a * b 
    def divide():
        return a / b
    return {
        'add_two_nums':add_two_nums,
        'multiply':multiply,
        'divide':divide
    }

print(do_math(2, 3)['add_two_nums']())
print(do_math(2, 3)['multiply']())
print(do_math(2, 3)['divide']())

# Functional Programming: map, filter, reduce