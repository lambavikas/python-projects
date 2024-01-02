import math

num1 = int(input("Enter first number: "))
op = input("Specify Operation [+  -   *   /]: ")
num2 = int(input("Enter second number: "))

if op == '+':
    print("Sum: " + str(math.add(num1, num2)))
elif op == '-':
    print("Diff: " + str(math.subtract(num1, num2)))
elif op == '*':
    print("Product: " + str(math.multiply(num1, num2)))
elif op == '/':
    print("Division: " + str(math.divideNew(num1, num2)))
else:
    print("Invalid Operation!")
