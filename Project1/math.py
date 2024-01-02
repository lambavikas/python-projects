def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        return 'Division By Zero Error!'


def divideNew(a, b):
    try:
        return a / b
    except ZeroDivisionError as err:
        print(err)
        return "Divide by Zero Not Possible!"