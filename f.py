import random # активація моодулю

def guess_the_number():
    number = random.randint(1, 10)
    print("Вгадай число від 1 до 10!") # задання функції і її граней

    while (guess := input("Введіть число: ")):
        guess = int(guess)
        if guess == number:
            print("Вітаємо! Ви вгадали!")
            break
        print("Більше!" if guess < number else "Менше!")
    else:
        print("Будь ласка, введіть ціле число.") # відповіді на на числа

guess_the_number() # виклик функції