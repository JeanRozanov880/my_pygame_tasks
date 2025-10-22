import pygame as pg

FPS = 60
WIN_WIDTH = 400
WIN_HEIGHT = 100
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)

pg.init()
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
screen.fill(WHITE)  # белый фон
pg.display.set_caption("Игра")
clock = pg.time.Clock()

# параметры квадрата
side = 40  # сторона квадрата
# начальные координаты левого верхнего угла квадрата:
x = 0  # начинаем у левой границы
y = WIN_HEIGHT // 2 - side // 2  # выравниваем по центру по вертикали

# параметры движения
direction = 1  # направление: 1 - вправо, -1 - влево
speed = 2  # начальная скорость
increase = 0.5  # насколько будет увеличиваться при отталкивании

# до начала игрового цикла отображаем объекты:
pg.draw.rect(screen, ORANGE, (x, y, side, side))  # рисуем квадрат
pg.display.update()  # обновляем окно

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

    # изменение состояний объектов:
    # проверяем достижение границ
    if x + side >= WIN_WIDTH:  # коснулись правой границы
        direction = -1  # меняем направление налево
        speed += increase
    elif x <= 0:  # коснулись левой границы
        direction = 1  # меняем направление направо
        speed += increase

    # перемещаем квадрат
    x += direction * speed


    screen.fill(WHITE)  # заливаем фон, стирая предыдущий квадрат
    pg.draw.rect(screen, ORANGE, (x, y, side, side))  # рисуем новый, сдвинутый квадрат

    pg.display.update()  # обновляем окно
