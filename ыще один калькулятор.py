import random
from collections import deque
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
    calculations.append((a, operator, b, result))
    return result
calculations = deque(maxlen=5)
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
random_calculator(num1, num2)
print("\nПоследние вычисления:")
for calc in calculations:
    print(f"{calc[0]} {calc[1]} {calc[2]} = {calc[3]}")