import random

mystery = random.randint(1,10)
print("Попробуйте угадать число от 1 до 10: ")
guess = int(input())
while guess != mystery:
    if guess < mystery:
        print("Число меньше загаданного, попробуйте ещё раз: ")
        guess = int(input())
    elif guess > mystery:
        print("Число больше загаданного, попробуйте ещё раз: ")
        guess = int(input())
print("Вы угадали!")