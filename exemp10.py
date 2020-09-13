from itertools import combinations, permutations
x = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
massiv = [y for y in x if x.count(y) == 1]
print(massiv)