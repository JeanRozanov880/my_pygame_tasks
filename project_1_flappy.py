import pygame as pg
import random

FPS = 60
W, H = 1000, 600
BG = (100, 170, 220)
speed = 3
gravity = 0.25
velocity = 0
jump_strength = -7


class Pipes:
    def __init__(self):
        self.origin_surf_1 = pg.image.load('pipe_for_flappy.png').convert_alpha()
        self.new_surf_1 = pg.transform.scale(self.origin_surf_1,
                                             (self.origin_surf_1.get_width() / 1.7,
                                              self.origin_surf_1.get_height() / 2))
        self.origin_rect_1 = self.new_surf_1.get_rect(center=(W / 1.2, H / 1.2))

        self.origin_surf_2 = pg.image.load('pipe_for_flappy.png').convert_alpha()
        self.new_surf_2 = pg.transform.scale(self.origin_surf_2,
                                             (self.origin_surf_2.get_width() / 1.7,
                                              self.origin_surf_2.get_height() / 2))
        self.final_surf_2 = pg.transform.rotate(self.new_surf_2, 180)
        self.origin_rect_2 = self.new_surf_1.get_rect(center=(W / 1.2, H / 6))

        self.mask_1 = pg.mask.from_surface(self.new_surf_1)
        self.mask_2 = pg.mask.from_surface(self.new_surf_2)

    def move(self, dx=0):
        if (self.origin_rect_1.left + dx * speed) < W:
            self.origin_rect_1.x += dx * speed
        if (self.origin_rect_2.left + dx * speed) < W:
            self.origin_rect_2.x += dx * speed

    def draw(self, screen):
        screen.blit(self.new_surf_1, self.origin_rect_1)
        screen.blit(self.final_surf_2, self.origin_rect_2)


class Bird:
    def __init__(self):
        self.origin_surf = pg.image.load('flappy_2.png').convert_alpha()
        self.new_surf = pg.transform.scale(self.origin_surf,
                                           (self.origin_surf.get_width() / 4,
                                            self.origin_surf.get_height() / 4))
        self.origin_rect = self.new_surf.get_rect(center=(W / 6, H / 2))
        self.mask = pg.mask.from_surface(self.new_surf)

    def move(self):
        global velocity
        velocity += gravity
        self.origin_rect.y += velocity

    def flap(self):
        global velocity
        velocity = jump_strength

    def draw(self, screen):
        screen.blit(self.new_surf, self.origin_rect)


def collisions(bird, pipes):
    offset_1 = (pipes.origin_rect_1.x - bird.origin_rect.x, pipes.origin_rect_1.y - bird.origin_rect.y)
    offset_2 = (pipes.origin_rect_2.x - bird.origin_rect.x, pipes.origin_rect_2.y - bird.origin_rect.y)

    if bird.mask.overlap(pipes.mask_1, offset_1) is not None:
        pg.quit()
    if bird.mask.overlap(pipes.mask_2, offset_2 ) is not None:
        pg.quit()


pg.init()
screen = pg.display.set_mode((W, H))
pg.display.set_caption("Игра")
clock = pg.time.Clock()

all_pipes = []

bird = Bird()
pipes = Pipes()

screen.fill(BG)
bird.draw(screen)
pipes.draw(screen)
pg.display.update()

flag_play = True
game_over = False

while flag_play:
    clock.tick(FPS)

    # цикл обработки событий:
    for event in pg.event.get():
        if event.type == pg.QUIT or game_over:
            pg.quit()
            flag_play = False
            break
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                bird.flap()
    if not flag_play:
        break

    new_pipe = Pipes()
    all_pipes.append(new_pipe)

    for pipe in all_pipes:
        pipe.move()

    if not game_over:
        bird.move()
        pipes.move(dx=-1)

    collisions(bird, pipes)

    screen.fill(BG)
    bird.draw(screen)
    pipes.draw(screen)
    pg.display.update()
