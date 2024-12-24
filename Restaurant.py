# Потоки гостей в кафе:

from threading import Thread
from time import sleep
from random import randint
from queue import Queue


class Table:
    """
    Столы в кафе:
    number - номер стола;
    guest - гость, который сидит за этим столом (по умолчанию None)
    """

    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):
    """
    Класс наследуется от класса Thread (является потоком):
    name - имя гостя;
    run - метод ожидания от 3 до 10 секунд (случайным образом).
    """

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    """
    Класс работы кафе, в котором есть определённое кол-во столов и происходит
    имитация прибытия гостей и их обслуживания:
    queue - очередь (объект класса Queue);
    tables - столы в кафе (любая коллекция);
    guest_arrival - прибытие гостей;
    discuss_guests - обслуживание гостей.
    """
    potoki = []

    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        """
        Функция, отражающая прибытие гостей в кафе.
        Принимает неограниченное кол-во гостей (объектов класса Guest).
        Если есть свободный стол, то сажает гостя за стол (назначает столу guest),
        запускает поток гостя и выводит на экран строку.
        Если свободных столов не осталось, то помещает гостя в очередь.
        """
        self.guests = guests
        min_ = min(len(self.guests), len(self.tables))
        for i in range(min_):
            self.tables[i].guest = self.guests[i]
            potok = self.guests[i]
            potok.start()
            Cafe.potoki.append(potok)
            print(f'{self.guests[i].name} сел(-а) за стол номер {self.tables[i].number}')
        if len(self.guests) > min_:
            for j in range(min_, len(self.guests)):
                self.queue.put(guests[j])
                print(f'{self.guests[j].name} в очереди')

    def discuss_guests(self):
        """
        Функция, отражающая обслуживание гостей в кафе.
        Обслуживание происходит, пока очередь не пустая (метод empty)
        или хотя бы один стол занят.
        Если за столом есть гость и он закончил приём пищи, стол освобождается (table.guest = None).
        Если очередь ещё не пуста (метод empty) и стол один из столов освободился (None),
        то текущему столу присваивается гость, взятый из очереди (queue.get()).
        Запускается поток этого гостя (start)
        """
        while not self.queue.empty() or not table.guest is None:
            for table in self.tables:
                if not table.guest is None and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                if not self.queue.empty() and table.guest is None:
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    potok = table.guest
                    potok.start()
                    Cafe.potoki.append(potok)


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()

for potok in Cafe.potoki:
    potok.join()
