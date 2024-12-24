# Соединение изображений

from PIL import Image


# открытие изображений
image1 = Image.open('IMG_0369.jpg')
image2 = Image.open("me.jpg")


# узнаем формат, размеры и цветовую гамму
print(image1.format, image1.size, image1.mode)
print(image2.format, image2.size, image2.mode)


# поворот изображения
image2 = image2.transpose(Image.Transpose.ROTATE_270)


def new_foto(new_image):
    """
    Обработка изображения (цвет, размер)
    """
    w, h = new_image.size
    new_image = new_image.resize((w // 2, h // 2)) # изменение размера
    new_image = new_image.convert('L') # изменение цвета на чб
    return new_image


def merge(img1, img2, img3):
    """
    Создание нового фото путем соединения нескольких:
    paste позволяет вставлять одно изображение в другое;
    box — координаты в виде кортежа, определяющего область вставки изображения.
    """
    w = img1.size[0] + img2.size[0]
    h = max(img1.size[1], img2.size[1])
    img = Image.new("RGBA", (w, h))
    img.paste(img1)
    img.paste(img2, (img1.size[0], 0))
    img.paste(img3, (0, 1200))
    return img


image1 = new_foto(image1)
image2 = new_foto(image2)
image3 = Image.open('hi.png')
image = merge(image1, image2, image3)
image.show()