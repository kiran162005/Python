# friends =  5

# friends = friends+1
# friends +=1

# friends = friends - 2
# friends -= 2

# friends = friends * 3
# friends *= 3

# friends = friends/2
# friends /= 2

# friends = friends ** 2
# friends **= 2
# reminder = friends % 2

# print(reminder)

'''
Docstring for 4_arthemetic
x = 3.14
y = 4
z = 5
result = round(x)
result1 = abs(y)
result2 = pow(3,4)

print(result)
print(result1)
print(result2)
print(max(x,y,z))
print(min(x,y,z))
'''

'''
import math

x = 9
print(math.pi)
print(math.e)
result = math.sqrt(x)
result = math.ceil(9.1)
result = math.floor(9.9)
print(result)
'''

import math

radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius
area = math.pi * pow(radius, 2)

print(f"The circumference is: {round(circumference, 2)}cm")
print(f"The area of the circle is: {round(area, 2)}cm^2")


a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side C = {c}")