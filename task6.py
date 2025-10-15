import pygame as pg

FPS = 60
WIN_WIDTH, WIN_HEIGHT = 1000, 600
BALL_WIDTH, BALL_HEIGHT = WIN_HEIGHT * 1 / 4, WIN_HEIGHT * 1 / 4
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
background = pg.Surface((WIN_WIDTH, WIN_HEIGHT))
background.fill(NIGHT_BLUE)
pg.draw.rect(background, DAY_BLUE, (0, WIN_HEIGHT * 3 / 14, WIN_WIDTH, WIN_HEIGHT * 1 / 5))
pg.draw.rect(background, DAY_BLUE, (0, WIN_HEIGHT * 3 / 5, WIN_WIDTH, WIN_HEIGHT * 1 / 5))

# слой №2 - первый шар
ball1 = pg.Surface((BALL_WIDTH, BALL_HEIGHT), pg.SRCALPHA)
ball1.fill((0, 0, 0, 0))  # сначала делаем всю поверхность полностью прозрачной
pg.draw.circle(ball1, (*RED, 100), (BALL_WIDTH / 2, BALL_HEIGHT / 2), r1)

# слой №3 - второй шар
ball2 = pg.Surface((BALL_WIDTH, BALL_HEIGHT), pg.SRCALPHA)
ball2.fill((0, 0, 0, 0))  # сначала делаем всю поверхность полностью прозрачной
pg.draw.circle(ball2, (*GREEN, 190), (BALL_WIDTH / 2, BALL_HEIGHT / 2), r2)

ball_x1, ball_y1 = 0, 0
ball_x2, ball_y2 = 0, 0
speed1 = 10
speed2 = 20

screen.blit(background, (0, 0))
screen.blit(ball1, (ball_x1, ball_y1))
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


    screen.blit(background, (0, 0))
    screen.blit(ball1, (ball_x1, ball_y1))
    pg.display.update()  # обновление экрана, чтобы отобразить новую перерисовку# задание на слои
