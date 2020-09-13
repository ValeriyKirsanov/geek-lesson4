massiv = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [
    value for idx, value in enumerate(massiv)
    if idx > 0 and massiv[idx - 1] < value
]
print(result)