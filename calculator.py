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

# Test the functions
result = add(5, 3)
print("5 + 3 =", result)

result = subtract(7, 2)
print("7 - 2 =", result)

result = multiply(4, 6)
print("4 * 6 =", result)

result = divide(8, 2)
print("8 / 2 =", result)
