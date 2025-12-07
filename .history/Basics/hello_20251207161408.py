# Comments

""" 
Package test

import requests

response = requests.get("https://api.github.com")
print(response.status_code)

200 is OK, 404 is Not Found

"""
# Single-line comments
# VS
# Multi-line comments

test1 = (
    "TEST 1"
    "TEST 2"
)

test2 = """
TEST 1
TEST 2
"""

# full name with underscore

long_dash = "-"

first_name = "John"
last_name = "Krak"

full_name = first_name + " " + last_name

dash_quantity = len(full_name)

underscore = long_dash * dash_quantity

full_name_plus_underscore = full_name + '\n'+underscore

print(full_name_plus_underscore)


Test = True
