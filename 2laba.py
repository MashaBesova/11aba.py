def z1():
    password = input("Введите пароль: ")
    confirm_password = input("Подтвердите пароль: ")
    if len(password) < 6:
        print("Пароль короткий")
    if password == confirm_password and len(password) >= 6:
        print("Пароль принят")
    else:
        print("Пароль не принят")

def z2():
    seat_number = int(input("Введите номер места: "))
    if seat_number < 1 or seat_number > 54:
        print("Неверный номер места")
    elif seat_number % 2 == 0:
        if seat_number <= 36:
            print("Верхнее место в купе")
        else:
            print("Верхнее место в боковом отсеке")
    else:
        if seat_number <= 36:
            print("Нижнее место в купе")
        else:
            print("Нижнее место в боковом отсеке")

def z3():
    g = int(input("Введите год "))
    if (g % 4 == 0 and g % 100!=0) or (g % 400 == 0):
        print(g, "високосный год")
    else:
        print(g, "не високосный год")

def z4():
    color1 = input("Введите первый цвет: ")
    color2 = input("Введите второй цвет: ")
    if color1 == "Красный" and color2 == "Синий" or color1 == "Синий" and color2 == "Красный":
        print("Фиолетовый")
    elif color1 == "Красный" and color2 == "Желтый" or color1 == "Желтый" and color2 == "Красный":
        print("Оранжевый")
    elif color1 == "Синий" and color2 == "Желтый" or color1 == "Желтый" and color2 == "Синий":
        print("Зеленый")
    else:
        print("Ошибка: введите названия цветов 'Красный', 'Синий' или 'Желтый'")

z1(), z2(), z3(), z4()