import math

def square(side):
    area = side * side
    # Если сторона не целая, результат может быть дробным — округляем вверх
    return math.ceil(area)

print(square(5))      # Ожидаем: 25
print(square(2.3))    # 2.3 * 2.3 = 5.29 → округляем вверх → 6
print(square(3.1))    # 3.1 * 3.1 = 9.61 → округляем вверх → 10
