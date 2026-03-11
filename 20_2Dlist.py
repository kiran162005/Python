
# fruits = ["apple", "orange", "banaga", "coconut"]
# vegetables = ["carrots", "potatoes", "beans"]
# meats = ["chicken", "fish", "turkey"]

# groceries = [fruits, vegetables, meats]
# print(groceries[1][1])


'''
groceries = [["apple", "orange", "banaga", "coconut"],
            ["carrots", "potatoes", "beans"],
            ["chicken", "fish", "turkey"]]

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()
'''

num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end= " ")
    print()