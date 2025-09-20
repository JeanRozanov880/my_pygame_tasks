import pygame as pg

# здесь определяются константы, функции и классы
FPS = 60
WIDTH, HEIGHT = 1000, 600
BLUE = (151, 210, 240)
BLACK = (0, 0, 0)
ORANGE = (238, 181, 50)
WHITE = (255, 255, 255)
BROWN = (97, 60, 52)
GRAY = (125, 125, 125)

# здесь происходит инициализация, создание объектов
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))  # также здесь можно указать битовые флаги
screen.fill(BLUE)
pg.display.set_caption("Игра")
clock = pg.time.Clock()

pg.draw.rect(screen, BLACK, (WIDTH / 2 - 300, HEIGHT / 2 - 20, 600, 270), 10)
pg.draw.lines(screen, BLACK, True, [(WIDTH / 2 - 300, HEIGHT / 2 - 20), (WIDTH / 2 + 300, HEIGHT / 2 - 20), (WIDTH / 2, HEIGHT / 2 - 200)], 10)
pg.draw.rect(screen, BLACK, (WIDTH / 2 - 150, HEIGHT / 2 + 50, 75, 75), 7)
pg.draw.rect(screen, BLACK, (WIDTH / 2 + 75, HEIGHT / 2 + 50, 75, 75), 7)
pg.draw.circle(screen, ORANGE, (100, 100), 50)
pg.draw.circle(screen, GRAY, (WIDTH / 2, HEIGHT / 2 + 50), 50)

pg.display.update()

# главный цикл
flag_play = True
while flag_play:
    # настраиваем частоту итераций в секунду
    clock.tick(FPS)

    # цикл обработки событий
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break
    if not flag_play:
        break

    # изменение объектов
    # ...

    # обновление экрана
    pg.display.update()
