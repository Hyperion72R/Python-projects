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

import statistics
import platform
import os
import json
import random
from math import sqrt, pi
import math
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
    numbers = [1, 2, 3, 4, 5, 6, 7]
    first_number = numbers[0]
    last_number = numbers[-1]
    return first_number, last_number

# f = first_number
# l = last_number


f, l = simple_function()

# print vs return


def get_greeting_print(name):
    print(f"Hello {name}!")
# Just displays


def get_greeting_return(name):
    return (f"Hello {name}!")


get_greeting_print("Anna")

get_greeting_return("Lola")

# add math module

math.sqrt(16)


sqrt(16)

# import math

# import random

# from math import sqrt

sqrt16 = sqrt(16)

number = random.randint(1, 10)

choice = random.choice(["apple", "bannana", "orange"])

# import datetime

today = datetime.date.today()

# time in Japan

# from datetime import datetime, timedelta


def godzina_w_japonii():
    utc_time = datetime.utcnow()
    tokyo_time = utc_time + timedelta(hours=9)
    return tokyo_time.strftime("%Y-%m-%d %H:%M:%S")


print("Aktualna godzina w Japonii:", godzina_w_japonii())

# JSON
# import json
person_date = {"name": "Anna", "age": 30}
json_string = json.dumps(person_date)


# OS

# import os

# prints the current working directory
# and lists all files and folders inside it.

current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

files = os.listdir(current_dir)
print("Files in directory:")
for f in files:
    print(f" - {f}")


# List files in a directory

# def list_files(path="."):
#     return os.listdir(path)

# import os


def list_files(path=".", count=True):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Path '{path}' does not exist")

    files = sorted(os.listdir(path))

# optional count parameter
    if count:
        return files, len(files)

    return files


# example
print(list_files())


# Check if a file exists

# import os

# Add try/except to handle OSError

def file_exists(filename):
    try:
        if os.path.isfile(filename):
            size = os.path.getsize(filename)
            return f"File exists. Size: {size} bytes"
        else:
            return "File does not exist"
    except OSError:
        return "Error accessing file"


print(file_exists("test.txt"))

# import os

# Checks if the given file exists.
# If it exists, returns its size in bytes.
# If it does not exist, returns an error message.


def file_size_check(name):
    if not os.path.isfile(name):
        return "File does not exist"
    size = os.path.getsize(name)
    return f"File size: {size} bytes"


print(file_size_check("test"))


# Returns basic operating system information (name, system, and release).
# If os.name is "nt", it replaces it with a more descriptive Windows name.
# When run directly, the script prints this information.

def system_name():
    """
    Returns basic information about the operating system.
    """
    os_name = os.name
    if os_name == "nt":
        os_name = "windows new technology"

    return {
        "os_name": os_name,
        "system": platform.system(),
        "release": platform.release()
    }


if __name__ == "__main__":
    info = system_name()
    print("Operating system info:")
    for key, value in info.items():
        print(f"{key}: {value}")


# Simple statistics function (statistics module)

# Calculates basic statistics (count, mean, median, min, max, std deviation)
# for a given list of numbers and returns them as a dictionary.


# import statistics


def basic_statistics(numbers):
    """
    Returns basic statistics for a list of numbers.
    """
    if not numbers:
        return "List is empty"

    try:
        mode_value = statistics.mode(numbers)
    except statistics.StatisticsError:
        mode_value = "No unique mode"

    return {
        "count": len(numbers),
        "mean": round(statistics.mean(numbers), 2),
        "median": statistics.median(numbers),
        "mode": mode_value,
        "min": min(numbers),
        "max": max(numbers),
        "std_dev": round(statistics.stdev(numbers), 2) if len(numbers) > 1 else 0
    }


# example
data = [117, 234, 532, 643, 436]

result = basic_statistics(data)

print("Statistics:")
for key, value in result.items():
    print(f"{key}: {value}")


# Prime number func

def is_prime(number=None):
    # If no number is provided, return a friendly message
    if number is None:
        return "Please provide a number to check."

    try:
        number = int(number)  # try to convert to integer
    except ValueError:
        return "Please enter a valid integer."

    if number < 2:
        return False  # Numbers less than 2 are not prime

    # Iterate from 2 up to the square root of the number (inclusive).
    # If the number has any divisor in this range, it is not prime.
    # We only check up to sqrt(number) because any larger factor
    # would have a corresponding smaller factor already checked.
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:   # Check if 'number' is divisible by i
            return False

    return True  # If no divisors were found, the number is prime


# Usage examples:
print(is_prime(7))      # True
print(is_prime())   # True
print(is_prime("a"))    # "Please enter a valid integer."


# Anomaly Detector
def find_anomalies(data):
    mean = sum(data) / len(data)
    std_dev = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
    anomalies = [x for x in data if abs(x - mean) > 2 * std_dev]
    return anomalies


# Example usage
dataset = [10, 12, 11, 13, 200, 12, 11]
print("Anomalies:", find_anomalies(dataset))
