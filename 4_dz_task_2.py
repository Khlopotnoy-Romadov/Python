#Задание 17
import random
mass = [random.randint(-10,10) for _ in range(10)]
minim = mass.index(min(mass))
maks = mass.index(max(mass))
if minim < maks:
    print(sum(mass[minim:maks])/len(mass[minim:maks]))
else:
    mass[minim] = (max(mass)+min(mass))/2
    mass[maks] = (max(mass)+min(mass))/2
    print(mass)

