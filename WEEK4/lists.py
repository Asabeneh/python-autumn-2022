
l = [1, 2, 3, 4, 5]
""" print(l)
print(len(l))
print(type(l))
print(l[0])
print(l[1])
print(l[2])
print(l[-1])
print(l[-5])
print(l[1:4])
print(l[3:])
print(l[:3])

print(list(range(6)))
print(list(range(50, 101, 5)))
evens = list(range(0, 101, 2))
odds = list(range(1, 51, 2))
print('Evens:', evens)
print('Odds:', odds)

print(sum(evens)) """

num1 = [1, 2, 3]
num2 = [4, 5, 6]
num3 = num1 + num2
print(num3)

nums = [-1, 2, 6, 3, 4, 0, ]
""" nums.append(5)
nums.append(6)
nums.append(7) """
print(nums)
# nums.pop()
# nums.pop(0)
print(nums)
""" nums.extend([20, 30, 50]) """
print(nums)
# nums.insert(2, 30)
print(nums)
# nums.remove(3)
print(nums)
# del nums[1:3]
print(nums)
nums_copy = nums.copy()
print(nums_copy)

nums.reverse()
print(nums)
nums.sort()
print(nums_copy)
print(nums)

nums.clear()
print(nums)

print('Asabeneh')