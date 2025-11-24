def choose_operation(func):
    def wrapper(first, second):
        if first < 0 or second < 0:
            operation = "*"
        elif first == second:
            operation = "+"
        elif first > second:
            operation = "-"
        else:
            operation = "/"
        result = func(first, second, operation)
        return result

    return wrapper


@choose_operation
def calc(first, second, operation):
    if operation == "+":
        return first + second
    elif operation == "-":
        return first - second
    elif operation == "*":
        return first * second
    elif operation == "/":
        return first / second


number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
print(calc(number1, number2))
