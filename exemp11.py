from functools import reduce

numbers = [x for x in range(100, 1001, 1) if x%2 == 0]

print(numbers)
plus = reduce(lambda a, b : a * b, numbers, 1)
print(plus)
