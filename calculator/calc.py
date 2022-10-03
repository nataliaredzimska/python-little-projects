def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def calc(a, b, operation):
    global result
    if operation == '+':
        result = add(a, b)
    elif operation == '-':
        result = sub(a, b)
    elif operation == '*':
        result = multiply(a, b)
    elif operation == '/':
        if b == 0:
            return 'You can\'t divide by zero.'
        result = divide(a, b)

    return float(result)

