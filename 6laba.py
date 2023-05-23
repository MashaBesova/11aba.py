def z1():
    countries_dict = {"Австрия": "Вена", "Бельгия": "Брюссель", "Великобритания": "Лондон", "Германия": "Берлин", "Ирландия": "Дублин","Лихтенштейн": "Вадуц", "Нидерладны": "Амстердам",
                  "Франция": "Париж", "Белоруссия": "Минск", "Болгария": "София", "Польша": "Варшава", "Чехия": "Прага", "Албания": "Тирана", "Босния и Герцеговина": "Сараево",
                  "Северная Македония": "Скопье", "Сербия": "Белград"}
    print(countries_dict)
    n=input("Введите название страны")
    print("Столица - ", countries_dict.get(n))
    for key in sorted(countries_dict):
        print(key, " - ", countries_dict[key])

def z2():
    alph = {
        "а": 1,
        "б": 3,
        "в": 1,
        "г": 3,
        "д": 2,
        "е": 1,
        "ё": 3,
        "ж": 5,
        "з": 5,
        "и": 1,
        "й": 4,
        "к": 2,
        "л": 2,
        "м": 2,
        "н": 1,
        "о": 1,
        "п": 2,
        "р": 1,
        "с": 1,
        "т": 1,
        "у": 2,
        "ф": 10,
        "х": 5,
        "ц": 5,
        "ч": 5,
        "ш": 8,
        "щ": 10,
        "ъ": 10,
        "ы": 4,
        "ь": 3,
        "э": 8,
        "ю": 8,
        "я": 3
    }
    n=input("Слово: ")
    sum=0
    for i in n:
        sum+=alph[i.lower()]
    print(sum)

def z3():
    students = {
        "Дима": ["Английский", "Испанский", "Французский"],
        "Никита": ["Английский", "Китайстай"],
        "Даша": ["Немецкий", "Французский", "Итальянский"],
        "Лиза": ["Испанский", "Китайский"]
    }
    all_languages = []
    for languages in students.values():
        all_languages.extend(languages)
    unique_languages = sorted(set(all_languages))
    print("Список всех языков:", unique_languages)
    chinese_speakers = []
    for name, languages in students.items():
        if "Китайский" in languages:
            chinese_speakers.append(name)
    print("Список студентов, знающих китайский язык:", chinese_speakers)
z1(), z2(), z3()
