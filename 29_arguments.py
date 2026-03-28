# default arguments = A default value for certain parameters
#                     default is used when that argument is omitted
#                     make your functions more flexible, reduces # of arguments
#                     1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary



# def net_price(list_price, discount, tax):
#     return list_price * (1 - discount) * (1 + tax)

# print(net_price(500, 0, 0.05))

# def net_price(list_price, discount=0, tax=0.05):
#     return list_price * (1 - discount) * (1 + tax)

# # print(net_price(500))
# print(net_price(500,0.1))

'''
import time

def count(end,start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!")

count(30, 15)
'''


# keyword arguments = an argument preceded by an identifier
# helps with readability
# order of arguments doesn't matter
# 1. positional 2. default 3. KEYWORD 4. arbitrary

'''def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello", title="Mr.", last="Squarepants", first="Spongebob")
'''

# for x in range(1,11):
#     print(x, end=" ")

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=91, area=123, first=456, last=7890)
print(phone_num)
