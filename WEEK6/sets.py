# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7}
# AUB = {1, 2, 3, 4, 5, 6, 7}
# AnB = {4, 5}
# A\B = {1, 2, 3}
# B\A = {6, 7}
# A Δ B = (A\B)u(B\A) = {1, 2, 3,6, 7}

# empty set

""" st = set()
print(st)
A = {1, 2, 3, 4, 5}
print(A)
print(type(A))
print(len(A))

for n in A:
    print(n) """


nums = {1, 2, 3}
nums.add(4)
nums.add(5)
nums.update([6, 7,8, 9, 10])

print(nums)

""" A = {1, 2, 3, 4, 5}
print('set:',A)
print('list:', list(A))
print('tuple:', tuple(A))
 """
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7}
AUB = A.union(B)
AnB = A.intersection(B)
print('A union B', AUB)
print('A intersection B', AnB)
A_without_B = A.difference(B)
B_without_A = B.difference(A)
print('A without B', A_without_B)
print('B without A', B_without_A)
symmetric_difference_of_AandB = A.symmetric_difference(B)
print(symmetric_difference_of_AandB)

# AUB = {1, 2, 3, 4, 5, 6, 7}
# AnB = {4, 5}
# A\B = {1, 2, 3}
# B\A = {6, 7}
# A Δ B = (A\B)u(B\A)

lst = ['Finnish', 'Finnish','Finnish', 'Swedish','Swedish','Swedish']
print(set(lst))

