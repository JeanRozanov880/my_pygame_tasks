import pygame as pg
import random

FPS = 60
WIDTH, HEIGHT = 600, 500
MINT = (230, 254, 212)
ORANGE = (255, 150, 100)
BLACK = (0, 0, 0)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Игра")
clock = pg.time.Clock()

# до начала игрового цикла отображаем объекты:
# координаты центра круга
x, y = WIDTH / 2, HEIGHT / 2  # координаты центра круга
r = 30  # радиус круга
cur_color = ORANGE  # текущий цвет круга
last_color_change = 0  # время последнего изменения цвета
delay = 500  # задержка между изменениями цвета в миллисекундах

pg.draw.circle(screen, cur_color, (x, y), r)  # рисуем круг
pg.display.update()  # обновляем окно

flag_play = True
while flag_play:
    clock.tick(FPS)
    cur_time = pg.time.get_ticks()  # получаем текущее время

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break
    if not flag_play:
        break

    # изменение состояний объектов:
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and x - r > 0:
        x -= 3
    if keys[pg.K_RIGHT] and x + r < WIDTH:
        x += 3
    if keys[pg.K_UP] and y - r > 0:
        y -= 3
    if keys[pg.K_DOWN] and y + r < HEIGHT:
        y += 3

    # проверяем нажатие пробела и задержку между изменениями цвета
    if keys[pg.K_SPACE] and cur_time - last_color_change > delay:
        # генерируем случайный цвет
        cur_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        last_color_change = cur_time  # обновляем время последнего изменения

    screen.fill(MINT)  # заливаем фон, стирая предыдущий круг
    pg.draw.circle(screen, cur_color, (x, y), r)  # рисуем новый, сдвинутый круг

    pg.display.update()  # обновляем окно
