def z1():
    n = int(input("Bведите число: "))
    if n % 3 == 0:
        print("Число",n, "делится на 3")
    else:
        print("Число не делится на 3")

def z2():
    try:
        n = int(input("Bедите чисcло: "))
        otv = 100 / n
    except ValueError:\
        print("Введено не число!")
    except ZeroDivisionError:\
        print("Ошибка! Введен ноль.")
    else:
        print("Результат деления:",otv)

def z3():
    d1 = input('Введите дату в формате дд/мм/гггг ')
    d2=d1.split("/")
    if (int(d2[0])*int(d2[1])) == (int(d2[2][2:4])):
        print("Дата",d1, "магическая!")
    else:
        print("дата не магическая")

def z4():
    try:
        b = input("Введите номер билета: ")
        k = 0
        k1 = 0
        if len(b) % 2 == 0:
            for i in b[0:int(len(b)/2)]:
                k=k+int(i)
            for i in b[int(len(b)/2):int(len(b))+1]:
                k1=k1+int(i)
            if k == k1:
                print("Билет",b, "счастливый!")
            else:
                print("Билет не счастливый")
        else:
            print("количество цифр нечетно.")
    except ValueError:
        print("Введите только числа")

z1(), z2(), z3(), z4()