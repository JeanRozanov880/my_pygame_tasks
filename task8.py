import pygame as pg
import random

FPS = 60
WIN_WIDTH, WIN_HEIGHT = 1000, 600
WHITE, BLACK, RED, BLUE = (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 65, 117)


class Food:
    RADIUS = 30

    def __init__(self, pos):
        self.surf = pg.Surface((Food.RADIUS * 2, Food.RADIUS * 2), pg.SRCALPHA)
        self.rect = self.surf.get_rect(center=pos)
        self.surf.fill((0, 0, 0, 0))
        pg.draw.circle(self.surf, (*BLACK, 255),
                       (self.rect.width / 2, self.rect.height / 2), self.RADIUS)
        self.mask = pg.mask.from_surface(self.surf)  # маска для бомбы
        self.active = True  # флаг активности еды

    def explode(self):
        self.surf.fill((0, 0, 0, 0))
        self.active = False  # деактивируем еду после съедания

    def draw(self, screen):
        if self.active:  # рисуем только активную еду
            screen.blit(self.surf, self.rect)


class Player:
    COLOR = (0, 0, 255)
    WIDTH, HEIGHT = 100, 200
    SPEED = 3
    PLAYER_RADIUS = 50

    def __init__(self):
        self.radius = Player.PLAYER_RADIUS
        # создаем начальную позицию и сразу инициализируем rect
        self.start_pos = (WIN_WIDTH / 2, WIN_HEIGHT / 2)
        self.surf = pg.Surface((self.radius * 2, self.radius * 2), pg.SRCALPHA)
        self.rect = self.surf.get_rect(center=self.start_pos)
        self.update_surface()
        self.speed = Player.SPEED
        self.mask = pg.mask.from_surface(self.surf)  # маска для игрока

    def update_surface(self):
        # сохраняем текущую позицию центра перед обновлением
        old_center = self.rect.center

        # обновляем поверхность игрока с новым радиусом
        self.surf = pg.Surface((self.radius * 2, self.radius * 2), pg.SRCALPHA)
        self.rect = self.surf.get_rect(center=old_center)
        self.surf.fill((0, 0, 0, 0))
        pg.draw.circle(self.surf, (*Player.COLOR, 255),
                       (self.rect.width / 2, self.rect.height / 2), self.radius)
        pg.draw.circle(self.surf, (*BLACK, 255),
                       (self.rect.width / 2, self.rect.height / 2), self.radius, 5)

    def grow(self, food_radius):
        # увеличиваем радиус игрока в зависимости от размера еды
        growth_factor = 0.5  # коэффициент роста (50% от радиуса еды)
        self.radius += int(food_radius * growth_factor)
        self.update_surface()
        self.mask = pg.mask.from_surface(self.surf)  # обновляем маску

    def move(self, dx=0, dy=0):
        if (self.rect.left + dx * self.speed) > 0 and (self.rect.right + dx * self.speed) < WIN_WIDTH:
            self.rect.x += dx * self.speed
        if (self.rect.top + dy * self.speed) > 0 and (self.rect.bottom + dy * self.speed) < WIN_HEIGHT:
            self.rect.y += dy * self.speed

    def draw(self, screen):
        screen.blit(self.surf, self.rect)


def check_collisions(player, bombs):
    # будем проверять пересечение маски игрока с масками бомб
    # так как порядок важен, пусть маска игрока будет первой маской, маска бомбы - второй
    for bomb in bombs:  # проверяем только активную еду
        if bomb.active:  # проверяем только активную еду
            offset = (bomb.rect.x - player.rect.x, bomb.rect.y - player.rect.y)  # вычисляем смещение
            # смещение указывает на сколько вторая маска смещена относительно первой
            if player.mask.overlap(bomb.mask, offset) is not None:  # проверяем пересечение первой маски со второй
                bomb.explode()
                player.grow(Food.RADIUS)  # увеличиваем радиус игрока


pg.init()
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pg.display.set_caption("Игра")
clock = pg.time.Clock()

bombs = [Food((random.randint(Food.RADIUS, WIN_WIDTH - Food.RADIUS),
               random.randint(Food.RADIUS, WIN_HEIGHT - Food.RADIUS)))
         for _ in range(3)]
player = Player()

screen.fill(WHITE)
for elem in bombs:
    elem.draw(screen)
player.draw(screen)
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

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        player.move(dx=-1)
    if keys[pg.K_RIGHT]:
        player.move(dx=1)
    if keys[pg.K_UP]:
        player.move(dy=-1)
    if keys[pg.K_DOWN]:
        player.move(dy=1)

    check_collisions(player, bombs)

    screen.fill(BLUE)
    for elem in bombs:
        elem.draw(screen)
    player.draw(screen)
    pg.display.update()
