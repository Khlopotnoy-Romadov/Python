import random

def passGener():
    password = ""
    k = 0
    while k != 10:
        password += str(chr(random.randint(33,126)))
        k += 1
    return password
print(passGener())

