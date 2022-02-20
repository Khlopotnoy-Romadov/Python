import math

print("Введите целое число, большее 500: ")
nubmer = int(input())
root = str(math.sqrt(nubmer))
if math.sqrt(nubmer).is_integer():
    print(math.sqrt(nubmer))
else:
    for i in range(len(root)):
        if root[i] == ".":
            print(root[:i+3])