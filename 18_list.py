#collection = single "variable" used to store multiple values
# List = [] ordered and changable, Duplicates ok
# Set = {} unordered and immutable. but add/remove OK. NO duplicates
# Tuple = () ordered and unchangable. Duplicates OK, Faster

"""
# List = [] ordered and changable, Duplicates ok
"""
# fruits = ["apple", "orange", "Banana", "Coconut"]
# print(dir(fruits))
# print(help(fruits))
# print(fruits[0])
# print(fruits[::2])
# print(fruits[::-1])

# for x in fruits:
#     print(x)

# print(len(fruits))
# print("apple" in fruits)

# fruits[0] = "pineapple"

# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.insert(0, "pineapple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("apple"))
# print(fruits.count("Banana"))
# print(fruits)


"""
# Set = {} unordered and immutable. but add/remove OK. NO duplicates
"""

# fruits = {"apple", "orange", "banana", "coconut", "coconut"}

# fruits.add("pineapple")
# fruits.remove("apple")
# # fruits.pop()
# # fruits.clear()
# print(fruits)


'''
# Tuple = () ordered and unchangable. Duplicates OK, Faster
'''
fruits = ("apple", "orange", "banana", "coconut")

# print(len(fruits))
# print("pineapple" in fruits)

print(fruits.index("banana"))
print(fruits.count("coconut"))

for fruit in fruits:
    print(fruit)