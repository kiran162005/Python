# Python writing files (.txt, .json, .csv)

# txt_data = "I like pizza!"
# employees = ["Alice", "Bob", "SAndy", "Sunny"]

# file_path = "output.txt"

'''
with open(file_path, "w") as file:
    file.write(txt_data)
    print(f"txt file '{file_path} was created")
'''

# try:
#     with open(file_path, "x") as file:
#         file.write(txt_data)
#         print(f"txt file '{file_path} was created")
# except:
#     print("That file already exists")

'''
with open(file_path, "a") as file:
    file.write("\n" + txt_data)
    print(f"txt file '{file_path} was created")
'''

# try:
#     with open(file_path, "w") as file:
#         for employee in employees:

#             file.write(employee + "\n")
#         print(f"txt file '{file_path} was created")
# except:
#     print("That file already exists")

'''
import json

employee = {
    "name" : "Spongebob",
    "age" : 30,
    "job": "cook"
}

