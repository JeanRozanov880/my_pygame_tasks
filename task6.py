import pygame as pg

FPS = 60
WIN_WIDTH, WIN_HEIGHT = 1000, 600
BALL_WIDTH, BALL_HEIGHT = WIN_HEIGHT * 1 / 4, WIN_HEIGHT * 1 / 1.6
NIGHT_BLUE = (14, 0, 77)
DAY_BLUE = (173, 203, 204)
RED = (255, 0, 0)
GREEN = (0, 201, 27)

pg.init()
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pg.display.set_caption("Игра")
clock = pg.time.Clock()

r1 = 50
r2 = 30

# слой №1 - фон и трубы
background_sf = pg.Surface((WIN_WIDTH, WIN_HEIGHT))
background_sf.fill(NIGHT_BLUE)
pg.draw.rect(background_sf, DAY_BLUE, (0, WIN_HEIGHT * 3 / 14, WIN_WIDTH, WIN_HEIGHT * 1 / 5))
pg.draw.rect(background_sf, DAY_BLUE, (0, WIN_HEIGHT * 3 / 5, WIN_WIDTH, WIN_HEIGHT * 1 / 5))

# слой №2 - первый шар
ball1_sf = pg.Surface((BALL_WIDTH, BALL_HEIGHT), pg.SRCALPHA)
ball1_sf.fill((0, 0, 0, 0))  # сначала делаем всю поверхность полностью прозрачной
pg.draw.circle(ball1_sf, (*RED, 70), (BALL_WIDTH / 2, BALL_HEIGHT / 2), r1)

# слой №3 - второй шар
ball2 = pg.Surface((BALL_WIDTH, BALL_HEIGHT), pg.SRCALPHA)
ball2.fill((0, 0, 0, 0))  # сначала делаем всю поверхность полностью прозрачной
pg.draw.circle(ball2, (*GREEN, 255), (BALL_WIDTH / 2, BALL_HEIGHT / 2), r2)

ball_x1, ball_y1 = 0, 0
ball_x2, ball_y2 = 0, 0
speed1 = 4
speed2 = 5
direction1 = 1 # направление (1-ого шара): 1 - вправо, -1 - влево
direction2 = 1 # направление (2-ого шара): 1 - вправо, -1 - влево

screen.blit(background_sf, (0, 0))
screen.blit(ball1_sf, (ball_x1, ball_y1))
screen.blit(ball2, (ball_x2, ball_y2))

pg.display.update()

# главный игровой цикл:
flag_play = True
while flag_play:
    clock.tick(FPS)  # настраиваем FPS (=частоту итераций в секунду)

    # цикл обработки событий:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break
    if not flag_play:
        break

    # изменение характеристик объектов:
    # обработка движения 1-го шара:
    if ball_x1 >= WIN_WIDTH + r1:
        direction1 = -1
        ball_y1 = BALL_HEIGHT / 1.6
    elif ball_x1 <= 0 - r1:  # достиг левой границы
        direction1 = 1  # меняем направление направо
        ball_y1 = 0  # поднимаем шар обратно
    ball_x1 += speed1 * direction1

    # обработка движения 2-го шара:
    if ball_x2 >= WIN_WIDTH + r2:
        direction2 = -1
        ball_y2 = BALL_HEIGHT / 1.6
    elif ball_x2 <= 0 - r2:
        direction2 = 1
        ball_y2 = 0
    ball_x2 += speed2 * direction2

    screen.blit(background_sf, (0, 0))
    screen.blit(ball1_sf, (ball_x1, ball_y1))
    screen.blit(ball2, (ball_x2, ball_y2))
    pg.display.update()  # обновление экрана, чтобы отобразить новую перерисовку
