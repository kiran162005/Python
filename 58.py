# Python reading files (.txt, .json, .csv)

'''
file_path = "C:/Users/Kiran T/python1/output.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found")

except PermissionError:
    print("YOu do not have permission to read that file")
'''

'''
import json

file_path = "C:/Users/Kiran T/python1/output.json"

try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content)
except FileNotFoundError:
    print("That file was not found")

except PermissionError:
    print("YOu do not have permission to read that file")
'''

import csv

file_path = "C:/Users/Kiran T/python1/output.csv"

