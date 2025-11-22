# главный файл:
import pygame as pg
from tests_game import Ball

FPS = 60
W, H = 700, 700
WHITE = (255, 255, 255)
BG = (105, 105, 105)
speed = 3

pg.init()
screen = pg.display.set_mode((W, H))
pg.display.set_caption("Игра")
balls = pg.sprite.Group()
balls.add(Ball(W // 2 + 250, speed - 2, 'red_car.png'))
balls.add(Ball(W // 2 - 30, speed - 1, 'blue_car.png'))
balls.add(Ball(W // 2 - 250, speed, 'yellow_car.png'))
clock = pg.time.Clock()

origin_surf = pg.image.load('car.png').convert_alpha()
origin_rect = origin_surf.get_rect(center=(W / 2, H / 2))

current_surf = origin_surf


# создаем спрайт для машины игрока
class PlayerCar(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = origin_surf
        self.rect = origin_rect
        self.mask = pg.mask.from_surface(self.image)  # создаем маску для точного определения коллизий


player_car = PlayerCar()


def flip1():
    global current_surf
    current_surf = pg.transform.rotate(origin_surf, -90)
    current_rect = current_surf.get_rect(center=origin_rect.center)
    player_car.image = current_surf
    player_car.rect = current_rect
    player_car.mask = pg.mask.from_surface(current_surf)  # обновляем маску после поворота
    return current_rect


def flip2():
    global current_surf
    current_surf = pg.transform.rotate(origin_surf, 90)
    current_rect = current_surf.get_rect(center=origin_rect.center)
    player_car.image = current_surf
    player_car.rect = current_rect
    player_car.mask = pg.mask.from_surface(current_surf)
    return current_rect


def flip3():
    global current_surf
    current_surf = pg.transform.rotate(origin_surf, 360)
    current_rect = current_surf.get_rect(center=origin_rect.center)
    player_car.image = current_surf
    player_car.rect = current_rect
    player_car.mask = pg.mask.from_surface(current_surf)
    return current_rect


def flip4():
    global current_surf
    current_surf = pg.transform.rotate(origin_surf, 180)
    current_rect = current_surf.get_rect(center=origin_rect.center)
    player_car.image = current_surf
    player_car.rect = current_rect
    player_car.mask = pg.mask.from_surface(current_surf)
    return current_rect


def move(dx=0, dy=0):
    global origin_rect
    if (origin_rect.left + dx * speed) > 0 and (origin_rect.right + dx * speed) < W:
        origin_rect.x += dx * speed
    if (origin_rect.top + dy * speed) > 0 and (origin_rect.bottom + dy * speed) < H:
        origin_rect.y += dy * speed
    player_car.rect = origin_rect  # обновляем позицию спрайта игрока


def draw_road_lines():
    pg.draw.rect(screen, WHITE, (W // 2 - 135, 0, 10, H))
    pg.draw.rect(screen, WHITE, (W // 2 + 135, 0, 10, H))


# главный игровой цикл:
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
    if not flag_play:
        break

    if not game_over:
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            move(dx=-1)
            origin_rect = flip2()
        if keys[pg.K_RIGHT]:
            move(dx=1)
            origin_rect = flip1()
        if keys[pg.K_UP]:
            move(dy=-1)
            origin_rect = flip3()
        if keys[pg.K_DOWN]:
            move(dy=1)
            origin_rect = flip4()

        balls.update(H)

        # проверка столкновений
        if pg.sprite.spritecollide(player_car, balls, False, pg.sprite.collide_mask):
            game_over = True

    screen.fill(BG)
    draw_road_lines()
    screen.blit(current_surf, origin_rect)
    balls.draw(screen)

    pg.display.update()  # обновление экрана, чтобы отобразить новую перерисовку
# модуль:
import pygame


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, speed, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, 0))
        self.speed = speed

    def update(self, *args):
        if self.rect.y < args[0] - 20:
            self.rect.y += self.speed
        else:
            self.rect.y = 0
