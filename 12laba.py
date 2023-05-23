
def z1():
    class IceCreamStand:
        def __init__(self, name, flavors):
            self.name = name
            self.flavors = flavors
        def show_flavors(self):
            print("Список доступных кусов мороженого:")
            for flavor in self.flavors:
                print("- " + flavor)
    my_stand = IceCreamStand("Мороженница ", ['фисташковое', 'шоколадное', 'ванильное', 'клубничное'])
    my_stand.show_flavors()
def z2():
    class IceCreamStand:
        def __init__(self, name, flavors, location, working_hours, type_flavors):
            self.name = name
            self.flavors = flavors
            self.location = location
            self.working_hours = working_hours
            self.type_flavors = type_flavors
        def show_flavors(self):
            print("Список доступных вкусов мороженого:")
            for flavor in self.flavors:
                print("- " + flavor)
        def add_flavor(self, flavor):
            self.flavors.append(flavor)
            print(f'Вкус {flavor} добавлен в список')
        def remove_flavor(self, flavor):
            if flavor in self.flavors:
                self.flavors.remove(flavor)
                print(f'Вкус {flavor} удален из списка')
            else:
                print(f'Вкус {flavor} не найден в списке')
        def check_flavor(self, flavor):
            if flavor in self.flavors:
                print(f'Вкус {flavor} есть в списке')
            else:
                print(f'Вкус {flavor} нет в списке')
        def describe_stand(self):
            print(f"Мороженница {self.name}")
            print(f"Место: {self.location}")
            print(f"Время работы: {self.working_hours}")
        def show_Typesflavors(self):
            print("Список доступных форм мороженого:")
            for types in self.type_flavors:
                print("- " + types)
    my_stand = IceCreamStand("Снежинка", ['фисташковое', 'шоколадное', 'ванильное', 'клубничное'], 'Большой Проспект Петроградской стороны', '10.00 - 22.00', ['стаканчик', 'трубочка', 'фруктоввый лед', 'эскимо'])
    my_stand.describe_stand()
    my_stand.show_flavors()
    my_stand.show_Typesflavors()
    my_stand.check_flavor("клубничное")
    my_stand.check_flavor("фисташковое")
    my_stand.add_flavor("фисташковое")
    my_stand.check_flavor("фисташковое")
    my_stand.remove_flavor("клубничное")
    my_stand.check_flavor("клубничное")

def z3():
    class IceCreamStand:
        def __init__(self, name, flavors):
            self.name = name
            self.flavors = flavors
        def get_menu(self):
            menu = "Добро пожаловать в мороженницу " + self.name + "\n"
            menu += "У нас есть такие вкусы мороженого:\n"
            for flavor in self.flavors:
                menu += "- " + flavor + "\n"
            return menu

    import tkinter as tk

    my_stand = IceCreamStand("Снежинка", ["ванильный", "фисташковый", "клубничный"])
    root = tk.Tk()
    root.title("Снежинка")
    menu_label = tk.Label(root, text=my_stand.get_menu())
    menu_label.pack()
    root.mainloop()
z1(), z2(), z3()