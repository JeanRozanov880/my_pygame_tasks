# Часть 1:

import pygame as pg
import random

FPS = 60
WIDTH, HEIGHT = 600, 500
MINT = (230, 254, 212)
ORANGE = (255, 150, 100)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Игра")
clock = pg.time.Clock()

# до начала игрового цикла отображаем объекты:
# координаты центра круга
r = 30
x, y = random.randint(0 + r, WIDTH - r), random.randint(0 + r, HEIGHT - r)  # координаты круга
pg.draw.circle(screen, ORANGE, (x, y), r)  # рисуем круг
pg.display.update()  # обновляем окно

flag_play = True
while flag_play:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
        if event.type == pg.MOUSEMOTION:
            mouse_pos = event.pos

            break
    if not flag_play:
        break

    # изменение состояний объектов:

    mouse_pos = pg.mouse.get_pos()
    dist = ((x - mouse_pos[0]) ** 2 + (y - mouse_pos[1]) ** 2) ** 0.5

    pressed = pg.mouse.get_pressed()
    if dist <= r:
        if pressed[1]:
            x, y = random.randint(0 + r, WIDTH - r), random.randint(0 + r, HEIGHT - r)
            screen.fill(MINT)
            pg.draw.circle(screen, ORANGE, (x, y), r)  # рисуем новый, сдвинутый круг
            pg.display.update()

    screen.fill(MINT)  # заливаем фон, стирая предыдущий круг
    pg.draw.circle(screen, ORANGE, (x, y), r)  # рисуем новый, сдвинутый круг
    pg.display.update()  # обновляем окно
