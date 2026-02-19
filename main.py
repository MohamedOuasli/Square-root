import math

num=float(input("Enter a number: "))

if num < 0:
    print("Square root does not exist for negative numbers.")
else:
    sqrt = math.sqrt(num)
    print("The square root is:", sqrt)