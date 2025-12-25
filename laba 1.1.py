import math

a = float(input("Введите длину первой стороны: "))
b = float(input("Введите длину второй стороны: "))
c = float(input("Введите длину третьей стороны: "))

if a + b > c and a + c > b and b + c > a:
    p = (a + b + c) / 2

    area = math.sqrt(p * (p - a) * (p - b) * (p - c))

    print(f"Площадь треугольника: {area:.2f}")
else:
    print("Треугольник с такими сторонами не существует")