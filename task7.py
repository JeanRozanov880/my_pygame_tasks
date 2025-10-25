import pygame as pg
import random as rnd

FPS = 60
WIN_WIDTH, WIN_HEIGHT = 1000, 600
NIGHT_BLUE = (14, 0, 77)
DAY_BLUE = (173, 203, 204)
RED = (255, 0, 0)
GREEN = (0, 201, 27)
RAND_COLOR = (rnd.randint(0, 255), rnd.randint(0, 255), rnd.randint(0, 255))


class Ball:

    def __init__(self):
        self.BALL_WIDTH, self.BALL_HEIGHT = WIN_HEIGHT * 1 / 4, WIN_HEIGHT * 1 / 1.6
        self.R1, self.R2, self.R3 = 50, 30, rnd.randint(25, 55)
        self.SPEED1, self.SPEED2, self.SPEED3 = 4, 5, rnd.randint(1, 6)
        self.DIR1, self.DIR2, self.DIR3 = 1, 1, 1

        self.surf1 = pg.Surface((self.BALL_WIDTH, self.BALL_HEIGHT), pg.SRCALPHA)
        self.surf2 = pg.Surface((self.BALL_WIDTH, self.BALL_HEIGHT), pg.SRCALPHA)
        self.surf3 = pg.Surface((self.BALL_WIDTH, self.BALL_HEIGHT), pg.SRCALPHA)

        self.rect1 = self.surf1.get_rect(centerx=WIN_WIDTH / 20)
        self.rect2 = self.surf2.get_rect(centerx=WIN_WIDTH / 20)
        self.rect3 = self.surf2.get_rect(centerx=WIN_WIDTH / 20)

        self.surf1.fill((0, 0, 0, 0))
        self.surf2.fill((0, 0, 0, 0))
        self.surf3.fill((0, 0, 0, 0))

        # первый шар:
        pg.draw.circle(self.surf1, (*RED, 70), (self.BALL_WIDTH / 2, self.BALL_HEIGHT / 2), self.R1)
        # второй шар:
        pg.draw.circle(self.surf2, (*GREEN, 255), (self.BALL_WIDTH / 2, self.BALL_HEIGHT / 2), self.R2)
        # рандомный шар:
        pg.draw.circle(self.surf3, (*RAND_COLOR, rnd.randint(0, 255)), (self.BALL_WIDTH / 2, self.BALL_HEIGHT / 2), self.R3)


    # движение первого шара:
    def move1(self):
        self.rect1.right += self.SPEED1 * self.DIR1

    # движение второго шара:
    def move2(self):
        self.rect2.right += self.SPEED2 * self.DIR2

    def move3(self):
        self.rect3.right += self.SPEED3 * self.DIR3

    def draw(self, screen):
        screen.blit(self.surf1, self.rect1)
        screen.blit(self.surf2, self.rect2)
        screen.blit(self.surf3, self.rect3)


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

    # обработка движения первого шара:
    if ball.rect1.right >= WIN_WIDTH + ball.R1 * 4:
        ball.DIR1 = -1
        ball.rect1.bottom = ball.BALL_HEIGHT * 1.61

    elif ball.rect1.left <= 0 - ball.R1:
        ball.DIR1 = 1
        ball.rect1.top = 0
    ball.move1()

    # обработка движения второго шара:
    if ball.rect2.right >= WIN_WIDTH + ball.R2 * 4:
        ball.DIR2 = -1
        ball.rect2.bottom = ball.BALL_HEIGHT * 1.61

    elif ball.rect2.left <= 0 - ball.R2:
        ball.DIR2 = 1
        ball.rect2.top = 0
    ball.move2()

    # обработка движения рандомного шара:
    pressed = pg.mouse.get_pressed()
    if pressed[0]:
        pg.draw.circle(ball.surf3, (*RAND_COLOR, rnd.randint(0, 255)), (ball.BALL_WIDTH / 2, ball.BALL_HEIGHT / 2),
                       ball.R3)
        if ball.rect3.right >= WIN_WIDTH + ball.R3 * 4:
            ball.DIR3 = -1
            ball.rect3.bottom = ball.BALL_HEIGHT * 1.61

        elif ball.rect3.left <= 0 - ball.R3:
            ball.DIR3 = 1
            ball.rect3.top = 0
        ball.move3()

    screen.blit(background_sf, (0, 0))
    ball.draw(screen)
    pg.display.update()
