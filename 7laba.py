from PIL import Image, ImageFilter

def z1():
    filename="sobaken.jpg"
    with Image.open(filename) as img:
        img.load()
    img.show()
    width, height = img.size
    format = img.format
    mode = img.mode
    print("Ширина: ", width)
    print("Высота: ", height)
    print("Формат: ", format)
    print("Цветовая модель: ", mode)

def z2():
    filename = "sobaken.jpg"
    with Image.open(filename) as img:
        img.load()
    new_img = img.resize((img.width//3, img.height//3))
    new_img.save("resize_sobaken.jpg")
    converted_img = img.transpose(Image.FLIP_TOP_BOTTOM)
    converted_img.save("flipsobaken_top_bottom.jpg")
    converted_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    converted_img.save("flipsobaken_left_right.jpg")

def z3():
    filenames = {"1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"}
    for file in filenames:
        with Image.open(file) as img:
            img.load()
            new_img = img.filter(ImageFilter.CONTOUR)
            new_img.show()
            new_img.save("new_" + file)

def z4():
    watermark="watermark.png"
    with Image.open(watermark) as img_watermark:
        img_watermark.load()
    img_watermark = Image.open(watermark)
    img_watermark = img_watermark.resize((img_watermark.width//2, img_watermark.height//2))
    new="sobaken.jpg"
    with Image.open(new) as img:
        img.load()
    img.paste(img_watermark, (300,200), img_watermark)
    img.save("watermarksobaken.jpg")

z1(), z2(), z3(), z4()