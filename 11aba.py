
def z1():
    class Restauraht:
        def __init__(self, name, cuisine):
            self.name = name
            self.cuisine = cuisine
        def discribe_restaurant(self):
            print(f"В ресторане {self.name} подают блюда {self.cuisine} кухни")
        def open_restaurant(self):
            print(f"{self.name} сейчас открыт!")
    newRestaurant = Restauraht("Токио", "Японской")
    print(newRestaurant.name)
    print(newRestaurant.cuisine)
    newRestaurant.discribe_restaurant()
    newRestaurant.open_restaurant()
# z2()
    newRestaurant1 = Restauraht("Круассан", "Французской")
    newRestaurant2 = Restauraht("Карри", "Индийской")
    newRestaurant3 = Restauraht("Буритто", "Мексиканской")
    newRestaurant1.discribe_restaurant()
    newRestaurant2.discribe_restaurant()
    newRestaurant3.discribe_restaurant()
def z3():
    class Restauraht:
        def __init__(self, name, cuisine, reting):
            self.name = name
            self.cuisine = cuisine
            self.reting = reting
        def discribe_restaurant(self):
            print(f"В ресторане {self.name} подают блюда {self.cuisine} кухни")
        def open_restaurant(self):
            print(f"{self.name} сейчас открыт!")
        def update_rating(self, new_rating):
            self.rating = new_rating
            print(f"Рейтинг ресторана {self.name} : {self.rating}.")

    newRestaurant = Restauraht("Токио", "Японской", 3.9)
    newRestaurant.discribe_restaurant()
    newRestaurant.update_rating(4.0)
    newRestaurant.discribe_restaurant()
z3()