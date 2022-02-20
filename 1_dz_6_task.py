import math

print("Выберите фигуру:\nКруг - 1\nТреугольник - 2\nПрямоугольник - 3")
figure = input()
if figure == "1":
    print("Введите радиус: ")
    r = int(input())
    print("Площадь круга: " + "pi" + str(r*r))
if figure == "2":
    print("Введите 1 сторону треугольника: ")
    a = int(input())
    print("Введите 2 сторону треугольника: ")
    b = int(input())
    print("Введите 3 сторону треугольника: ")
    c = int(input())
    p = (a+b+c)/2
    S = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("Площадь треугольника: " + str(S))
if figure == "3":
    print("Введите длину 1 стороны: ")
    one = int(input())
    print("Введите длину 2 стороны: ")
    two = int(input())
    print(one*two)