import tkinter
import os
from tkinter import filedialog


def file_select():
    """
    Функция работы с диалоговыми окнами:
    initialdir задает начальную директорию - путь, указывающий на расположение файлов;
    filetypes - для фильтрации типов файлов;
    filename хранит путь к выбранному файлу;
    text['text'] - информация о выбранном файле (название и полный путь) на виджете;
    os.startfile(filename) - запуск файла
    """
    filename = filedialog.askopenfilename(initialdir='/', title='Выберите файл',
                                          filetypes=(('Текстовый файл', '.txt'), ('Все файлы', '*')))
    text['text'] = text['text'] + ' ' + filename
    os.startfile(filename)


# Отрисовка окна

window = tkinter.Tk()
window.title('Проводник')  # Название окна
window.geometry('450x150')  # Размер окна
window.configure(bg='violet')  # Цвет фона
window.resizable(False, False)  # Запрет изменять размер

# текстовое поле с информацией, какой файл открыт
text = tkinter.Label(window, text='Файл', height=5, width=65, background='silver',
                     foreground='black')
text.grid(column=1, row=1)

# Кнопка открытия файла
button_select = tkinter.Button(window, width=20, height=3, text='Выбрать файл',
                               background='silver', foreground='black',
                               command=file_select)
button_select.grid(column=1, row=2, pady=5)

window.mainloop()
