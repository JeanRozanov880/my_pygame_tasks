import pygame as pg

FPS = 60
W, H = 1000, 600
BG = (100, 170, 220)
speed = 3

pg.init()
screen = pg.display.set_mode((W, H))
pg.display.set_caption("Игра")
clock = pg.time.Clock()

origin_surf = pg.image.load('car.png').convert_alpha()
origin_rect = origin_surf.get_rect(center=(W / 2, H / 2))

current_surf = origin_surf


def flip1():
    global current_surf
    current_surf = pg.transform.rotate(origin_surf, -90)
    current_rect = current_surf.get_rect(center=origin_rect.center)
    return current_rect


def flip2():
    global current_surf
    current_surf = pg.transform.rotate(origin_surf, 90)
    current_rect = current_surf.get_rect(center=origin_rect.center)
    return current_rect


def flip3():
    global current_surf
    current_surf = pg.transform.rotate(origin_surf, 360)
    current_rect = current_surf.get_rect(center=origin_rect.center)
    return current_rect


def flip4():
    global current_surf
    current_surf = pg.transform.rotate(origin_surf, 180)
    current_rect = current_surf.get_rect(center=origin_rect.center)
    return current_rect


def move(dx=0, dy=0):
    global origin_rect
    if (origin_rect.left + dx * speed) > 0 and (origin_rect.right + dx * speed) < W:
        origin_rect.x += dx * speed
    if (origin_rect.top + dy * speed) > 0 and (origin_rect.bottom + dy * speed) < H:
        origin_rect.y += dy * speed


# главный игровой цикл:
flag_play = True
while flag_play:
    clock.tick(FPS)

    # цикл обработки событий:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break
    if not flag_play:
        break

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        move(dx=-1)
        origin_rect = flip2()
    elif keys[pg.K_RIGHT]:
        move(dx=1)
        origin_rect = flip1()
    elif keys[pg.K_UP]:
        move(dy=-1)
        origin_rect = flip3()
    elif keys[pg.K_DOWN]:
        move(dy=1)
        origin_rect = flip4()

    screen.fill(BG)
    screen.blit(current_surf, origin_rect)
    pg.display.update()  # обновление экрана, чтобы отобразить новую перерисовку
