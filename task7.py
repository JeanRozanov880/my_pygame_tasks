import pygame as pg
import random as rnd

FPS = 60
WIN_WIDTH, WIN_HEIGHT = 1000, 600
NIGHT_BLUE = (14, 0, 77)
DAY_BLUE = (173, 203, 204)
RED = (255, 0, 0)
GREEN = (0, 201, 27)


class Ball:
    def __init__(self, ball_type="random"):
        self.BALL_WIDTH, self.BALL_HEIGHT = WIN_HEIGHT * 1 / 4, WIN_HEIGHT * 1 / 1.6

        if ball_type == "ball_1":
            self.R = 50
            self.SPEED = 4
            self.COLOR = (*RED, 70)
        elif ball_type == "ball_2":
            self.R = 30
            self.SPEED = 5
            self.COLOR = (*GREEN, 255)
        else:  # random
            self.R = rnd.randint(25, 55)
            self.SPEED = rnd.randint(1, 6)
            self.COLOR = (*(rnd.randint(0, 255), rnd.randint(0, 255), rnd.randint(0, 255)),
                          rnd.randint(50, 255))

        self.DIR = 1

        self.surf = pg.Surface((self.BALL_WIDTH, self.BALL_HEIGHT), pg.SRCALPHA)
        self.surf.fill((0, 0, 0, 0))

        # рисуем шар
        pg.draw.circle(self.surf, self.COLOR, (self.BALL_WIDTH / 2, self.BALL_HEIGHT / 2), self.R)

        # позиционируем шар в начале верхней трубы
        self.rect = self.surf.get_rect(centerx=WIN_WIDTH / 20)

        # для рандомного шара устанавливаем начальную позицию как у других
        if ball_type == "random":
            self.rect = self.surf.get_rect(centerx=WIN_WIDTH / 20)

    def move(self):
        self.rect.right += self.SPEED * self.DIR

    def draw(self, screen):
        screen.blit(self.surf, self.rect)

    def update(self):
        # обработка движения шара
        if self.rect.right >= WIN_WIDTH + self.R * 4:
            self.DIR = -1
            self.rect.bottom = self.BALL_HEIGHT * 1.61
        elif self.rect.left <= 0 - self.R:
            self.DIR = 1
            self.rect.top = 0
        self.move()


pg.init()
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pg.display.set_caption("Игра")
clock = pg.time.Clock()

background_sf = pg.Surface((WIN_WIDTH, WIN_HEIGHT))
background_sf.fill(NIGHT_BLUE)
pg.draw.rect(background_sf, DAY_BLUE, (0, WIN_HEIGHT * 3 / 14, WIN_WIDTH, WIN_HEIGHT * 1 / 5))
pg.draw.rect(background_sf, DAY_BLUE, (0, WIN_HEIGHT * 3 / 5, WIN_WIDTH, WIN_HEIGHT * 1 / 5))

# Создаем начальные шары
balls = [Ball("ball_1"), Ball("ball_2")]

screen.blit(background_sf, (0, 0))
for ball in balls:
    ball.draw(screen)
pg.display.update()

flag_play = True
mouse_pressed_prev = False  # для отслеживания нажатия кнопки мыши

while flag_play:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break

    if not flag_play:
        break

    # проверяем нажатие левой кнопки мыши
    mouse_pressed = pg.mouse.get_pressed()[0]

    # если кнопка только что нажата (а не удерживается)
    if mouse_pressed and not mouse_pressed_prev:
        # Создаем новый рандомный шар
        new_ball = Ball("random")
        balls.append(new_ball)

    mouse_pressed_prev = mouse_pressed

    # Обновляем все шары
    for ball in balls:
        ball.update()

    # отрисовываем
    screen.blit(background_sf, (0, 0))
    for ball in balls:
        ball.draw(screen)
    pg.display.update()
