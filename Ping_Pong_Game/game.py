import arcade

SCREEN_WIDTH = 800 # ширина окна
SCREEN_HEIGHT = 600 # высота окна
SCREEN_TITLE = 'Pong game' # заголовок окна


class Ball(arcade.Sprite):
    """
    Класс для мяча:
    - в init подгружаем изображение и устанавливаем размер;
    - функция update отвечает за логику движения (в т.ч. ограничение по границам окна).
    """
    def __init__(self):
        super().__init__('ball.png', 0.04)
        self.change_x = 4
        self.change_y = 4

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.right >= SCREEN_WIDTH:
            self.change_x = -self.change_x
        if self.left <= 0:
            self.change_x = -self.change_x
        if self.top >= SCREEN_HEIGHT:
            self.change_y = -self.change_y
        if self.bottom <= 0:
            self.change_y = -self.change_y


class Bar(arcade.Sprite):
    """
    Класс для ракетки:
    - в init подгружаем изображение и устанавливаем размер;
    - функция update отвечает за логику движения (в т.ч. ограничение по границам окна).
    """
    def __init__(self):
        super().__init__('bar.png', 0.35)
        self.change_x = 3

    def update(self):
        self.center_x += self.change_x
        if self.right >= SCREEN_WIDTH:
            self.change_x = -self.change_x
        if self.left <= 0:
            self.change_x = 0


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.ball = Ball()
        self.bar = Bar()
        self.setup() # не метод Windows, поэтому вызываем

    def setup(self):
        """
        Положение элементов в игре.
        """
        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = SCREEN_HEIGHT / 5
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 2

    def on_draw(self):
        """
        Отрисовка элементов на окне игры:
        clear - очистка окна (закрашивание окна белым);
        draw отрисовывает ракетку и мячик.
        """
        self.clear((255, 255, 255))
        self.ball.draw()
        self.bar.draw()

    def update(self, delta):
        """
        Обновление информации о текущем состоянии элемента (запуск методов Sprites)
        arcade.check_for_collision проверяет Sprites на столкновение и отталкивает мяч
        """
        if arcade.check_for_collision(self.bar, self.ball):
            self.ball.change_y = -self.ball.change_y
        self.ball.update()
        self.bar.update()

    def on_key_press(self, key, modifiers):
        """
        Управление ракеткой с помощью клавиатуры (нажатие кнопки) - движение.
        """
        if key == arcade.key.RIGHT:
            self.bar.change_x = 5
        if key == arcade.key.LEFT:
            self.bar.change_x = -5

    def on_key_release(self, key, modifiers):
        """
        Управление ракеткой с помощью клавиатуры (отпускание кнопки) - остановка
        """
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.bar.change_x = 0


if __name__ == '__main__':
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)  # окно игры
    arcade.run()  # цикл обновления
