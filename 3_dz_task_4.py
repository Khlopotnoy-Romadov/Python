import random

def passGener():
    password = ""
    k = 0
    while k != 10:
        password += str(chr(random.randint(33,126)))
        k += 1
    return password

def safePass(password):
    if len(password) >= 8 and password.islower() == False and password.isupper() == False:
        for i in range(len(password)):
            if password[i].isdigit():
                return True
    return False

def combo():
    count = 1
    while safePass(passGener()) != True:
        count +=1
    return count
print(combo())