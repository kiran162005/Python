# List comprehension = A concise way to create lists in Python
# Compact and easier to read than traditional loops
# [expression for value in iterable if condition]

'''
doubles = []
for x in range(1, 11):
    doubles.append(x * 2)

print(doubles)
'''

'''
doubles = [x * 2 for x in range(1,11)]
triples = [y * 3 for y in range(1,11)]
squares = [z ** 2 for z in range(1,11)]

print(doubles)
print(triples)
print(squares)
'''

'''
fruits = ["apple", "orange", "banana", "coconut"]
fruit_chars = [fruit[0] for fruit in fruits]
fruits = [fruit.upper() for fruit in fruits]
