def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, "y", 2))


x = "abcd"

print(x[0])
