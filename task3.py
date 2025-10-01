import pygame as pg

FPS = 60
WIN_WIDTH = 700
WIN_HEIGHT = 400
BLUE = (0, 108, 163)
BLACK = (0, 0, 0)

pg.init()
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
screen.fill(BLUE)  # белый фон
pg.display.set_caption("Игра")
clock = pg.time.Clock()

# параметры квадрата
w = 120  # ширина эллипса
h = 60  # высота эллипса
# начальные координаты левого верхнего угла квадрата:
x = 0  # начинаем у левой границы
y = 0

# параметры движения
direction = 1  # направление: 1 - вправо, -1 - влево, -2 - вверх, 2 - вниз
speed = 3  # начальная скорость

# до начала игрового цикла отображаем объекты:
pg.draw.ellipse(screen, BLACK, (x, y, w, h))  # рисуем эллипс
pg.display.update()  # обновляем окно

flag_play = True
while flag_play:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break
    if not flag_play:
        break

    # изменение состояний объектов:
    # проверяем достижение границ

    if x + w >= WIN_WIDTH:  # коснулись правой границы
        direction = 2  # меняем направление вниз
    elif y + h >= WIN_HEIGHT:  # коснулись низа
        direction = -1  # меняем направление влево
    elif x <= 0:  # коснулись левой границы
        direction = -2  # меняем направление вверх
    else:
        direction = 1



    screen.fill(BLUE)  # заливаем фон, стирая предыдущий эллипс
    pg.draw.ellipse(screen, BLACK, (x, y, w, h))  # рисуем новый, сдвинутый эллипс

    pg.display.update()  # обновляем окно
