#Задание 5
import random

words = ["самовар", "весна", "лето"]
word = random.choice(words)
symbol = random.choice(word)
guess = input()
print("You win") if guess == symbol else print("You lose")

