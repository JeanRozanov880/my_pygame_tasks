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
r = 35
inc = 1 # насколько будем увеличивать
min_r = 10
max_r = 120
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
        if event.type == pg.MOUSEWHEEL: # изменяем размеры шара с помощью колесика
            if event.y > 0: # увеличиваем шар
                if r < max_r:
                    r += inc
            if event.y < 0: # уменьшаем шар
                if r > min_r:
                    r -= inc

            break
    if not flag_play:
        break

    # изменение состояний объектов:

    mouse_pos = pg.mouse.get_pos()
    dist = ((x - mouse_pos[0]) ** 2 + (y - mouse_pos[1]) ** 2) ** 0.5

    pressed = pg.mouse.get_pressed()
    if dist <= r: # проверяем, наведена ли мышь на шар
        if pressed[1]: # при нажатии на колесико шар лопается и отрисовывается новый
            x, y = random.randint(0 + r, WIDTH - r), random.randint(0 + r, HEIGHT - r)

        if pressed[0]: # увеличение шара на м1
            if r < max_r:
                r += inc
                
        if pressed[2]: # уменьшение шара на м2
            if r > min_r:
                r -= inc

    screen.fill(MINT)  # заливаем фон, стирая предыдущий круг
    pg.draw.circle(screen, ORANGE, (x, y), r)  # рисуем новый, сдвинутый круг
    pg.display.update()  # обновляем окно
