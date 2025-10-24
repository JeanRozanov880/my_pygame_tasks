import pygame as pg
import random

FPS = 60
WIN_WIDTH, WIN_HEIGHT = 1000, 600
NIGHT_BLUE = (14, 0, 77)
DAY_BLUE = (173, 203, 204)
RED = (255, 0, 0)
GREEN = (0, 201, 27)


class Ball:

    BALL_WIDTH, BALL_HEIGHT = WIN_HEIGHT * 1 / 4, WIN_HEIGHT * 1 / 1.6
    SPEED1, SPEED2 = 4, 5
    R1, R2 = 50, 30
    DIR1, DIR2 = 1, 1

    def __init__(self):
        self.surf = pg.Surface((Ball.BALL_WIDTH, Ball.BALL_HEIGHT), pg.SRCALPHA)
        self.rect = self.surf.get_rect(centerx=WIN_WIDTH / 20)
        self.surf.fill((0, 0, 0, 0))
        # первый шар:
        pg.draw.circle(self.surf, (*RED, 70), (Ball.BALL_WIDTH / 2, Ball.BALL_HEIGHT / 2), Ball.R1)
        # vtoroi shar:
        pg.draw.circle(self.surf, (*GREEN, 255), (Ball.BALL_WIDTH / 2, Ball.BALL_HEIGHT / 2), Ball.R2)

    # движение первого шара:
    def move_right1(self):
        if self.rect.right >= WIN_WIDTH + Ball.R1:
            self.DIR1 = -1
            self.rect.bottom = Ball.BALL_HEIGHT * 1.61
        self.rect.right += Ball.SPEED1 * Ball.DIR1

    def move_left1(self):
        if self.rect.left <= 0 - Ball.R1:
            self.DIR1 = 1
            self.rect.top = 0
        self.rect.right += Ball.SPEED1 * Ball.DIR1

    # движение второго шара:
    def move_right2(self):
        if self.rect.right >= WIN_WIDTH + Ball.R2:
            self.DIR2 = -1
            self.rect.bottom = Ball.BALL_HEIGHT * 1.61
        self.rect.right += Ball.SPEED2 * Ball.DIR2

    def move_left2(self):
        if self.rect.left <= 0 - Ball.R2:
            self.DIR2 = 1
            self.rect.top = 0
        self.rect.right += Ball.SPEED2 * Ball.DIR2

    def draw(self, screen):
        screen.blit(self.surf, self.rect)


pg.init()
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # экран
pg.display.set_caption("Игра")
clock = pg.time.Clock()

background_sf = pg.Surface((WIN_WIDTH, WIN_HEIGHT))
background_sf.fill(NIGHT_BLUE)
pg.draw.rect(background_sf, DAY_BLUE, (0, WIN_HEIGHT * 3 / 14, WIN_WIDTH, WIN_HEIGHT * 1 / 5))
pg.draw.rect(background_sf, DAY_BLUE, (0, WIN_HEIGHT * 3 / 5, WIN_WIDTH, WIN_HEIGHT * 1 / 5))

ball = Ball()

screen.blit(background_sf, (0, 0))
ball.draw(screen)
pg.display.update()

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

    ball.move_right1()
    ball.move_left1()
    ball.move_right2()
    ball.move_left2()

    screen.blit(background_sf, (0, 0))
    ball.draw(screen)
    pg.display.update()
  # НАДО СДЕЛАТЬ ДВА RECT-а И ВОЗМОЖНО ДВА SURFACE
