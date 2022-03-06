#Задание 6
import math

def my_log(lst: list) -> list:
    return [math.log(x) if x > 0 else None for x in lst]
print(my_log([4,6,1,9,0,-4,6,-1]))
