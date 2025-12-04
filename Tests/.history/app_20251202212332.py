def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, "y", 2))


x = "*"*10

x2 = len(x)

print(x2)
