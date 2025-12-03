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
        rand_height_1 = random.randint(200, 400)

        self.origin_surf_1 = pg.image.load('images/pipe_for_flappy.png').convert_alpha()
        self.new_surf_1 = pg.transform.scale(self.origin_surf_1,
                                             (self.origin_surf_1.get_width() / 1.7,
                                              self.origin_surf_1.get_height() / 2))
        self.origin_rect_1 = self.new_surf_1.get_rect(midtop=(W + 100, rand_height_1))

        self.origin_surf_2 = pg.image.load('images/pipe_for_flappy.png').convert_alpha()
        self.new_surf_2 = pg.transform.scale(self.origin_surf_2,
                                             (self.origin_surf_2.get_width() / 1.7,
                                              self.origin_surf_2.get_height() / 2))
        self.final_surf_2 = pg.transform.rotate(self.new_surf_2, 180)
        self.origin_rect_2 = self.final_surf_2.get_rect(midbottom=(W + 100, rand_height_1 - 150))

        self.mask_1 = pg.mask.from_surface(self.new_surf_1)
        self.mask_2 = pg.mask.from_surface(self.final_surf_2)

    def move(self):
        self.origin_rect_1.x -= speed
        self.origin_rect_2.x -= speed

    def draw(self, screen):
        screen.blit(self.new_surf_1, self.origin_rect_1)
        screen.blit(self.final_surf_2, self.origin_rect_2)

    def is_offscreen(self):
        return self.origin_rect_1.x < 0


class Bird:
    def __init__(self):
        self.origin_surf = pg.image.load('images/flappy_2.png').convert_alpha()
        self.new_surf = pg.transform.scale(self.origin_surf,
                                           (self.origin_surf.get_width() / 6,
                                            self.origin_surf.get_height() / 6))
        self.origin_rect = self.new_surf.get_rect(center=(W / 6, H / 2))
        self.mask = pg.mask.from_surface(self.new_surf)

    def move(self):
        global velocity, gravity
        velocity += gravity
        self.origin_rect.y += velocity

    def flap(self):
        global velocity
        velocity = jump_strength

    def draw(self, screen):
        screen.blit(self.new_surf, self.origin_rect)

    def check_pos(self):
        if self.origin_rect.bottom > H + self.new_surf.get_height() / 3:
            pg.quit()
        if self.origin_rect.top <= 0 - self.new_surf.get_height() / 3:
            pg.quit()


def collisions(bird, pipes_list):
    for pipes in pipes_list:
        offset_1 = (pipes.origin_rect_1.x - bird.origin_rect.x, pipes.origin_rect_1.y - bird.origin_rect.y)
        offset_2 = (pipes.origin_rect_2.x - bird.origin_rect.x, pipes.origin_rect_2.y - bird.origin_rect.y)

        if bird.mask.overlap(pipes.mask_1, offset_1) is not None:
            pg.quit()
        if bird.mask.overlap(pipes.mask_2, offset_2) is not None:
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
SPAWN_EVENT = pg.USEREVENT + 1
pg.time.set_timer(SPAWN_EVENT, 1500)

while flag_play:
    clock.tick(FPS)

    # цикл обработки событий:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                bird.flap()
        if event.type == SPAWN_EVENT:
            all_pipes.append(Pipes())

    bird.move()

    for elem in all_pipes[:]:
        elem.move()

    all_pipes = [pipes for pipes in all_pipes if not pipes.is_offscreen()]

    collisions(bird, all_pipes)
    bird.check_pos()

    screen.fill(BG)
    for elem in all_pipes:
        elem.draw(screen)
    bird.draw(screen)
    pg.display.update()
