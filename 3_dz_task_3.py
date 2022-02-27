password1 = ""

def safePass(password):
    if len(password) >= 8 and password.islower() == False and password.isupper() == False:
        for i in range(len(password)):
            if password[i].isdigit():
                return True
    return False
print(safePass(password1))
