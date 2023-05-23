from PIL import Image, ImageDraw, ImageFont

def z1():
    image = Image.open('sobaken.jpg')
    cropped_image= image.crop((50,100,800,800))
    cropped_image.save('cropped_sobacen.jpg')

def z2():
    greetings={
        "Новый год": "newyear.jpg",
        "День рождения": "happybithday.jpg",
        "8 марта": "8march.jpg",
        "23 февраля": "23february.jpg"
    }
    holiday = input("Введите название праздника: ")
    if holiday in greetings:
        image= Image.open (greetings[holiday])
        image.show()
    else:
        print ("Открытки для такого праздника нет")

def z3():
    greetings = {
        "Новый год": "newyear.jpg",
        "День рождения": "happybithday.jpg",
        "8 марта": "8march.jpg",
        "23 февраля": "23february.jpg"
    }
    holiday = input("Введите название праздника: ")
    if holiday in greetings:
        image= Image.open (greetings[holiday])
        name = input("Введите имя человека, которого хотите поздравить: ")
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("arial.ttf", 80)
        text = f"{name}, поздравляю!"
        text_windth, text_height = draw.textsize(text, font)
        x=(image.width -text_windth)/2
        y=image.height - text_height - 50
        draw.text((x,y), text, font=font, fill=(255, 0, 0, 255))
        image.show()
        image.save("greeting.jpg")
    else:
        print ("Открытки для такого праздника нет")

z1(), z2(), z3()
