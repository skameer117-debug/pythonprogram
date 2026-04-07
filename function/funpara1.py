def multiply(*args):
    result = 1
    for num in args:
        result*= num
print(multiply(2, 3))
print(multiply(2, 3, 4))
print(multiply(1, 2, 3, 4, 5))