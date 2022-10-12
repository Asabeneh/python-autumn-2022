def add_two_nums(a, b):
    return a + b
def make_square(n):
    return n ** 2
def add_all_nums(n):
    total = 0
    if n > 0:
        for i in range(n+1):
            total = total + i
    else:
        for i in range(n, 0):
            total = total + i
    return total

def generate_evens(end, start = 0):
    if start % 2 == 0:
        evens = list(range(start, end + 1, 2))
        return evens
    else:
        evens = list(range(start + 1, end + 1, 2))
        return evens

