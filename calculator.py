def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def power(base, exponent):
    return base ** exponent

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Test the functions
result = add(5, 3)
print("5 + 3 =", result)

result = subtract(7, 2)
print("7 - 2 =", result)

result = multiply(4, 6)
print("4 * 6 =", result)

result = divide(8, 2)
print("8 / 2 =", result)

result = power(2, 3)
print("2 ^ 3 =", result)

result = divide(8, 0)
print("8 / 0 =", result)

result = factorial(5)
print("Factorial of 5 =", result)