from PIL import Image, ImageFilter
import csv
from pathlib import Path

def z1():

    x = ["1.png","2.jpg","3.png","4.jpg","5.png"]
    count = 0
    for file in x:
        if file.endswith('.jpg') or file.endswith('.png'):
            count += 1
            img = Image.open(file)
            newimg = img.filter(ImageFilter.EMBOSS)
            newimg.show()
            try:
                os.mkdir("F:/Универ/Програмирование")
            except:
                pass
            newimg.save(f"F:/Универ/Програмирование/new_img{count}.png")

def z3():
    with open('93.csv', 'r') as f:
        data = []
        for line in f:
            parts = line.strip().split(',')
            if len(parts) == 3:
                data.append(parts)
    total_price = 0
    print('Нужно купить:')
    for item in data[1:]:
        product = item[0]
        quantity = int(item[1])
        price = int(item[2])
        item_price = quantity * price
        total_price += item_price
        print('{} - {} шт. за {} руб.'.format(product, quantity, item_price))
    print('Итоговая сумма: {} руб.'.format(total_price))

z1(), z3()