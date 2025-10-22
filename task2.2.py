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
direction_x = 1  # направление по X: 1 - вправо, -1 - влево
direction_y = 0  # направление по Y: 1 - вниз, -1 - вверх
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

    if x + w >= WIN_WIDTH and direction_x == 1:  # коснулись правой границы, летим вниз
        direction_x = 0
        direction_y = 1

    elif y + h >= WIN_HEIGHT and direction_y == 1:  # коснулись нижней границы, летим влево
        direction_x = -1
        direction_y = 0

    elif x <= 0 and direction_x == -1:
        direction_x = 0
        direction_y = -1

    elif y <= 0 and direction_y == -1:
        direction_x = 1
        direction_y = 0

    x += direction_x * speed
    y += direction_y * speed


    screen.fill(BLUE)  # заливаем фон, стирая предыдущий эллипс
    pg.draw.ellipse(screen, BLACK, (x, y, w, h))  # рисуем новый, сдвинутый эллипс

    pg.display.update()  # обновляем окно
