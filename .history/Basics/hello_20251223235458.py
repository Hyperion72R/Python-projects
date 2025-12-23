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

# booleans

Test = True

Test2 = False

X = Test or Test2

# string manipulation

name = "John"

string = f"Hi there, my name is {name}"

string.title()

# if statements

temperature_check = False

temperature = 11

""" 
if temperature > 25:
    print("It's very hot!")
elif temperature > 25:
    print("It's hot!")
else:
    print("It's nice weather!")
"""

if temperature_check:
    if temperature >= 25:
        print("enjoy the weather!")
    else:
        print("need to wait")
else:
    print("the thermometer doesn't work")


# loops

for i in range(5):
    print(i, "test")


# Data structures

# list

age = 25

has_licence = False

my_list = ["Alice", 25, age, True, has_licence]

name = my_list[0]

has_license = my_list[-1]

my_list[0] = "Anna"


my_list.append("Alice")

my_list.insert(1, "Alice")

my_list.remove(25)


# dictionaries

person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}


person["age"] = 30


# tuples

empty = ()

point = (3, 5)

colors = ("red", "blue", "green")

print(point[0])


# sets


empty_set = set()

number = {1, 2, 3}

fruits = set(["apple", "orange", "plum"])


scores = [1, 2, 3, 4, 5, 6, 7, 7, 7]

uniqe_scores = set(scores)


# Functions

def greet():
    print("Hello!")


greet()


def calculate_total():
    pass


calculate_total()


def check_weather():
    if temperature > 25:
        print("It's hot!")
    else:
        print("It's nice weather!")
