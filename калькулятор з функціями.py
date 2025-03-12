import random

def random_calculator(a, b):
    operators = ['+', '-', '*']
    operator = random.choice(operators)

    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    else:
        result = a * b

    print(f"{a} {operator} {b} = {result}")
    return result

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
random_calculator(num1, num2)