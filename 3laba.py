def z1():
    N = int(input("Введите количество слов: "))
    words = []
    for i in range(N):
        word = input("Введите слово: ")
        words.append(word)
    result = " ".join(words)
    print(result)

def z2():
    words = []
    while True:
        word = input("Введите слово: ")
        if word == "stop":
            break
        words.append(word)
    result = " ".join(words)
    print(result)

def z3():
    word = input("Введите слово: ")
    if "ф" in word:
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")

def z4():
    import random
    correct_answers = 0
    mistakes = 0
    while mistakes < 3:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        expression = str(a) + " + " + str(b) + " = "
        answer = input(expression)
        if int(answer) == a + b:
            print("Правильно!")
            correct_answers += 1
        else:
            print("Ответ неверный")
            mistakes += 1
    print("Игра окончена. Правильных ответов:", correct_answers)

z1(), z2(), z3(), z4()