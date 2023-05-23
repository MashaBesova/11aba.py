def z1():
    numbers = [2, 5, 8, 10, 13]
    user_num = int(input("Введите число: "))
    if user_num in numbers:
        print("Поздравляю, Вы угадали число!")
    else:
        print("Нет такого числа!")
    print("Исходный список:", numbers)
    print("Число пользователя:", user_num)
def z2():
    my_list = [2, 5, 8, 2, 13]
    for num in my_list:
        if my_list.count(num) > 1:
            print(num)
            break
def z3():
    week_days = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")
    weekend_num = int(input("Сколько выходных дней на неделе вы хотите? "))
    weekend_days = week_days[-weekend_num:]
    work_days = week_days[:-weekend_num]
    print("Ваши выходные дни:", ", ".join(weekend_days))
    print("Ваши рабочие дни:", ", ".join(work_days))
def z4():
    group1 = ["Иванов", "Петров", "Сидоров", "Козлов", "Новиков", "Смирнов", "Кузнецов", "Морозов", "Волков", "Зайцев"]
    group2 = ["Соколова", "Кузьмина", "Иванова", "Петрова", "Сидорова", "Козлова", "Новикова", "Смирнова", "Морозова",
              "Волкова"]
    team = (group1[:5] + group2[:5])
    print("Исходные списки групп:")
    print("Группа 1:", group1)
    print("Группа 2:", group2)
    print("Спортивная команда:", team)
    print("Длина команды:", len(team))
    sorted_team = sorted(team)
    print("Отсортированная команда:", sorted_team)
    ivanov_count = team.count("Иванов")
    if ivanov_count > 0:
        print("Студент Иванов входит в команду")
        print("Количество студентов с фамилией Иванов в команде:", ivanov_count)
    else:
        print("Студент Иванов не входит в команду")

z1(), z2(), z3(), z4()