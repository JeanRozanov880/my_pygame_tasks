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
ball1_rect = ball1_sf.get_rect(centerx=WIN_WIDTH / 20)
ball1_sf.fill((0, 0, 0, 0))  # сначала делаем всю поверхность полностью прозрачной
pg.draw.circle(ball1_sf, (*RED, 70), (BALL_WIDTH / 2, BALL_HEIGHT / 2), r1)

# слой №3 - второй шар
ball2_sf = pg.Surface((BALL_WIDTH, BALL_HEIGHT), pg.SRCALPHA)
ball2_rect = ball2_sf.get_rect(centerx=WIN_WIDTH / 20)
ball2_sf.fill((0, 0, 0, 0))  # сначала делаем всю поверхность полностью прозрачной
pg.draw.circle(ball2_sf, (*GREEN, 255), (BALL_WIDTH / 2, BALL_HEIGHT / 2), r2)

speed1 = 4
speed2 = 5
direction1 = 1 # направление (1-ого шара): 1 - вправо, -1 - влево
direction2 = 1 # направление (2-ого шара): 1 - вправо, -1 - влево

screen.blit(background_sf, (0, 0))
screen.blit(ball1_sf, ball1_rect)
screen.blit(ball2_sf, ball2_rect)

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
    # движение 1-ого шара:
    if ball1_rect.right >= WIN_WIDTH + r1: # если шар дошел до правой границы
        direction1 = -1 # меняем направление налево
        ball1_rect.bottom = BALL_HEIGHT * 1.61 # переносим вниз
    elif ball1_rect.left <= 0 - r1: # если шар дошел до левой границы
        direction1 = 1 # меняем направление направо
        ball1_rect.top = 0 # переносим вверх (исходное положение)
    ball1_rect.right += speed1 * direction1 # обработка самого движения
        
    # движение 2-ого шара (аналогично первому):
    if ball2_rect.right >= WIN_WIDTH + r2:
        direction2 = -1
        ball2_rect.bottom = BALL_HEIGHT * 1.61
    elif ball2_rect.left <= 0 - r2:
        direction2 = 1
        ball2_rect.top = 0
    ball2_rect.right += speed2 * direction2

    screen.blit(background_sf, (0, 0))
    screen.blit(ball1_sf, ball1_rect)
    screen.blit(ball2_sf, ball2_rect)
    pg.display.update()  # обновление экрана, чтобы отобразить новую перерисовку
