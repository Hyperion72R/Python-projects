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


def check_weather(temperature):
    if temperature > 25:
        print("It's hot!")
    else:
        print("It's nice weather!")


check_weather(27)


def greet(name):
    print(f"Hello, {name}")


greet("Alice")

greet(name="Anna")

# name = n
# lastName = ln
# l = location


def greet2(n, ln="Kama", l="Madera"):
    print(f"Hello, {n} {ln} from {l}")


# greet2()
# reverse order

greet2(ln="Nana", n="Nadia")


# calculator


# Global variable vs local variable
# difference in discount variable

# global variable
discount = 20


def calculate_total(price, tax_rate, discount):
    tax_rate = 0.08
    # local variable
    discount = 10

    tax = price * tax_rate
    final_price = price + tax - discount
    # return round(final_price, 2)

    print(f"Total: ${final_price}")


discount

total = calculate_total(price=100, tax_rate=0.08, discount=10)


# return value from function

def add_print(a, b):
    print(a+b)


add_print(a=5, b=10)


def add_return(a, b, c):
    return a + b + c


result = add_return(a=5, b=10, c=10)

result + 20


def calculate_area(width, height):
    area = width * height

    return area


room_area = calculate_area(10, 12)

print(f"Room size: {room_area} sq ft")

print("interactive session vs terminal")


# add_print is visible in the terminal
def add_print(a, b):
    print(a+b)


print_result = add_print(a=5, b=10)
#  variable print_result is not visible in interactive session


# add_return is not visible in the terminal
def add_return(a, b):
    return a+b


result = add_return(a=5, b=10)
# variable result is visible in interactive session


# Using return values


def double(number):
    return number * 2


# Store in variable
result = double(5)

# Use in expressions
total = double(5) + double(3)

# pass to other functions
print(double(10))

# Use in conditions
if double(7) > 10:
    print("Big number")


def simple_function():
    number = [1, 2, 3, 4, 5, 6, 7]
    first_number = number[0]
    last_number = number[-1]
    return first_number, last_number
