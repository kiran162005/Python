# name = input("Enter your full name: ")

# result = len(name)
# print(name.find("r"))
# print(name.rfind("r"))
# name = name.capatalize()
# name = name.upper()
# name = name.lower()
# result = name.isdigit()
# result = name.isalpha()

# print(result)
'''
phone = input("Enter your phone number: ")

res = phone.count("-")
print(res)

phone = phone.replace("-"," ")
print(phone)
'''

# print(help(str))


#validate user input
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits


'''
username = input("Enter a username: ")


if len(username) > 12:
    print("Username can't be more than 12 characters")
elif not username.find(" ") == 1:
    print("Your username cant contain spaces")
elif not username.isalpha():
    print("Your username cant contain numbersk")
else:
    print(f"Welcome {username}")
'''


#indexing = accessing elements of a sequence using [] (indexing operator)
            # [start : end : step]

credit_number = "1234-5678-9012-3456"

# print(credit_number[4])
# print(credit_number[:4])
# print(credit_number[5:9])
# print(credit_number[5:])
# print(credit_number[-3])
# print(credit_number[::3])

last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")