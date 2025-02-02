import os
import sys
import pygame
import random
import time
import pygame_menu
import pygame_widgets
from pygame_widgets.slider import Slider


# Создание правил
def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    FPS = 10
    screen = pygame.display.set_mode((900, 630))
    pygame.init()
    clock = pygame.time.Clock()
    intro_text = ["БОУЛИНГ", "",
                  "Правила игры:",
                  "Сбей все кегли",
                  "Управление: кнопки A D и стрелочки < >",
                  "что бы кинуть шар нажмите мышкой на кнопку start game",
                  "НАЖМИТЕ ЛЮБУЮ КНОПКУ ЧТО БЫ ПРОДОЛЖИТЬ!"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (900, 630))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


# загрузка изображений
def load_image(name, colorkey=None):
    screen = pygame.display.set_mode((900, 630))
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


# class Menu():
#     # создаём список меню, с расположением, именем, цветом, цвет выбранного меню
#     # номер пункта
#     def __init__(self, punkts=[120, 140, u"punkt", (250, 250, 30), (250, 30, 250)]):
#         # передаём список команде Punkts
#         self.punkts = punkts
#
#     # отображаем повержность, где будем рисовать, экземпляр шрифта,номер активного элеменат
#     def render(self, poverhost, font, num_punkt):
#         # цикл фор, кот перебирает совпадает ли номер переданной функций
#         # если совпадает, то закрашивается цветом активного элемента
#         for i in self.punkts:
#             if num_punkt == i[5]:
#                 poverhost.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
#             else:
#                 poverhost.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))
#
#     # Основная функция, которая реализует систему меню
#     def menu(self):
#         done = True
#         # задаём шрифт
#         font_menu = pygame.font.SysFont("Blackoak Std", 60)
#         # деактивируем залипание клавишщь чтобы работала кнопка ESCAPE
#         pygame.key.set_repeat(0, 0)
#         # Делаем видимый курсор в меню
#         pygame.mouse.set_visible(True)
#         # хранение и использование переменной
#         punkt = 0

# Создание кегль
class Pin(pygame.sprite.Sprite):
    normal_im = load_image("kegl.png")
    fall_im = load_image("kegl4.png")

    def __init__(self, group, x, y):
        super().__init__(group)

        self.image = Pin.normal_im

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# Создание шара для боулинга
class Bowl(pygame.sprite.Sprite):
    image = load_image("1free-bowling-alley-background-vector.png")

    def __init__(self, group, x, y):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно !!!
        # размер окна у меня 500 на 500
        super().__init__(group)
        self.image = Bowl.image
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (900, 630))
        self.rect.topleft = (x, y)

        self.velocity = random.randint(1, 5)
        self.xx = 200
        self.yy = 300

        self.r = 0


# Создание кнопки start game
def draw_button(text_in_button):
    font = pygame.font.Font(None, 24)
    button_surface = pygame.Surface((150, 50))
    text = font.render(text_in_button, True, (255, 255, 255))
    text_rect = text.get_rect(
        center=(button_surface.get_width() / 2,
                button_surface.get_height() / 2))
    button_rect = pygame.Rect(370, 550, 150, 50)
    button_surface.blit(text, text_rect)
    screen.blit(button_surface, (button_rect.x, button_rect.y))

    return button_rect


# отрисовка таблицы
def Draw_tabl():
    draw_button(text_in_button)
    pygame.draw.rect(screen, (255, 255, 255),
                     (350, 10, 240, 80))
    # горизонатлные линии
    pygame.draw.line(screen, (0, 0, 0), [350, 50], [590, 50], 3)
    pygame.draw.line(screen, (0, 0, 0), [392, 10], [392, 90], 3)
    pygame.draw.line(screen, (0, 0, 0), [430, 10], [430, 90], 3)
    pygame.draw.line(screen, (0, 0, 0), [470, 10], [470, 90], 3)
    pygame.draw.line(screen, (0, 0, 0), [510, 10], [510, 90], 3)
    pygame.draw.line(screen, (0, 0, 0), [550, 10], [550, 90], 3)

    # вертикальные линии
    pygame.draw.line(screen, (0, 0, 0), [350, 10], [390, 50], 4)
    pygame.draw.line(screen, (0, 0, 0), [391, 10], [431, 50], 4)
    pygame.draw.line(screen, (0, 0, 0), [430, 10], [470, 50], 4)
    pygame.draw.line(screen, (0, 0, 0), [470, 10], [510, 50], 4)
    pygame.draw.line(screen, (0, 0, 0), [510, 10], [550, 50], 4)
    pygame.draw.line(screen, (0, 0, 0), [550, 10], [590, 50], 4)

    pygame.draw.rect(screen, (255, 255, 255),
                     (610, 10, 50, 50))


# подсчет результатов в таблице
def Draw_chifr_tabl(numbet_udar, round, proverka_ydar):
    global text_ydar1, text_ydar2, text_ydar3, text_ydar4, text_ydar5, text_ydar6, text_ydar1_2, text_ydar2_2, \
        text_ydar3_2, text_ydar4_2, text_ydar5_2, text_ydar6_2
    global text_sum_ydar1, text_sum_ydar2, text_sum_ydar3, text_sum_ydar4, text_sum_ydar5, text_sum_ydar6
    global ostatok
    f1 = pygame.font.Font(None, 30)
    if numbet_udar == 2 and round == 1:
        proverka_ydar[0] = True
        ostatok = len(pin_group)
        if len(pin_group) == 0:
            ydar1 = f"X"
        elif len(pin_group) == 10:
            ydar1 = f"-"
        else:
            ydar1 = f"{10 - len(pin_group)}"
        text_ydar1 = f1.render(ydar1, True,
                               (0, 0, 0))
    if numbet_udar == 3 and round == 1:
        proverka_ydar[1] = True

        if ostatok - len(pin_group) != 0:
            ydar1_2 = f"{ostatok - len(pin_group)}"
        elif len(pin_group) == 0:
            ydar1_2 = f"X"
        else:
            ydar1_2 = f"-"
        sum_ydar1 = f"{10 - len(pin_group)}"
        text_sum_ydar1 = f1.render(sum_ydar1, True,
                                   (0, 0, 0))
        text_ydar1_2 = f1.render(ydar1_2, True,
                                 (0, 0, 0))
    if numbet_udar == 2 and round == 2:
        proverka_ydar[2] = True
        ostatok = len(pin_group)
        if len(pin_group) == 0:
            ydar2 = f"X"
        elif len(pin_group) == 10:
            ydar2 = f"-"
        else:
            ydar2 = f"{10 - len(pin_group)}"
        text_ydar2 = f1.render(ydar2, True,
                               (0, 0, 0))
    if numbet_udar == 3 and round == 2:
        proverka_ydar[3] = True
        if ostatok - len(pin_group) != 0:
            ydar2_2 = f"{ostatok - len(pin_group)}"
        elif len(pin_group) == 0:
            ydar2_2 = f"X"
        else:
            ydar2_2 = f"-"
        sum_ydar2 = f"{10 - len(pin_group)}"
        text_sum_ydar2 = f1.render(sum_ydar2, True,
                                   (0, 0, 0))
        text_ydar2_2 = f1.render(ydar2_2, True,
                                 (0, 0, 0))
    if numbet_udar == 2 and round == 3:
        proverka_ydar[4] = True
        ostatok = len(pin_group)
        if len(pin_group) == 0:
            ydar3 = f"X"
        elif len(pin_group) == 10:
            ydar3 = f"-"
        else:
            ydar3 = f"{10 - len(pin_group)}"
        text_ydar3 = f1.render(ydar3, True,
                               (0, 0, 0))
    if numbet_udar == 3 and round == 3:
        proverka_ydar[5] = True
        if ostatok - len(pin_group) != 0:
            ydar3_2 = f"{ostatok - len(pin_group)}"
        elif len(pin_group) == 0:
            ydar3_2 = f"X"
        else:
            ydar3_2 = f"-"
        sum_ydar3 = f"{10 - len(pin_group)}"
        text_sum_ydar3 = f1.render(sum_ydar3, True,
                                   (0, 0, 0))
        text_ydar3_2 = f1.render(ydar3_2, True,
                                 (0, 0, 0))
    if numbet_udar == 2 and round == 4:
        proverka_ydar[6] = True
        ostatok = len(pin_group)
        if len(pin_group) == 0:
            ydar4 = f"X"
        elif len(pin_group) == 10:
            ydar4 = f"-"
        else:
            ydar4 = f"{10 - len(pin_group)}"
        text_ydar4 = f1.render(ydar4, True,
                               (0, 0, 0))
    if numbet_udar == 3 and round == 4:
        proverka_ydar[7] = True
        if ostatok - len(pin_group) != 0:
            ydar4_2 = f"{ostatok - len(pin_group)}"
        elif len(pin_group) == 0:
            ydar4_2 = f"X"
        else:
            ydar4_2 = f"-"
        sum_ydar4 = f"{10 - len(pin_group)}"
        text_sum_ydar4 = f1.render(sum_ydar4, True,
                                   (0, 0, 0))
        text_ydar4_2 = f1.render(ydar4_2, True,
                                 (0, 0, 0))
    if numbet_udar == 2 and round == 5:
        proverka_ydar[8] = True
        ostatok = len(pin_group)
        if len(pin_group) == 0:
            ydar5 = f"X"
        elif len(pin_group) == 10:
            ydar5 = f"-"
        else:
            ydar5 = f"{10 - len(pin_group)}"
        text_ydar5 = f1.render(ydar5, True,
                               (0, 0, 0))
    if numbet_udar == 3 and round == 5:
        proverka_ydar[9] = True
        if ostatok - len(pin_group) != 0:
            ydar5_2 = f"{ostatok - len(pin_group)}"
        elif len(pin_group) == 0:
            ydar5_2 = f"X"
        else:
            ydar5_2 = f"-"
        sum_ydar5 = f"{10 - len(pin_group)}"
        text_sum_ydar5 = f1.render(sum_ydar5, True,
                                   (0, 0, 0))
        text_ydar5_2 = f1.render(ydar5_2, True,
                                 (0, 0, 0))
    if numbet_udar == 2 and round == 6:
        proverka_ydar[10] = True
        ostatok = len(pin_group)
        if len(pin_group) == 0:
            ydar6 = f"X"
        elif len(pin_group) == 10:
            ydar6 = f"-"
        else:
            ydar6 = f"{10 - len(pin_group)}"
        text_ydar6 = f1.render(ydar6, True,
                               (0, 0, 0))
    if numbet_udar == 3 and round == 6:
        proverka_ydar[11] = True
        if ostatok - len(pin_group) != 0:
            ydar6_2 = f"{ostatok - len(pin_group)}"
        elif len(pin_group) == 0:
            ydar6_2 = f"X"
        else:
            ydar6_2 = f"-"
        sum_ydar6 = f"{10 - len(pin_group)}"
        text_sum_ydar6 = f1.render(sum_ydar6, True,
                                   (0, 0, 0))
        text_ydar6_2 = f1.render(ydar6_2, True,
                                 (0, 0, 0))

    text_sum_all = f1.render("TTL", True,
                             (0, 0, 0))
    screen.blit(text_sum_all, (610, 10))
    text_sum_all_col = f1.render(f"{sum_total}", True,
                                 (0, 0, 0))
    screen.blit(text_sum_all_col, (610, 30))
    if proverka_ydar[0]:
        screen.blit(text_ydar1, (360, 28))
    if proverka_ydar[1]:
        screen.blit(text_ydar1_2, (375, 10))
        screen.blit(text_sum_ydar1, (360, 60))
    if proverka_ydar[2]:
        screen.blit(text_ydar2, (400, 27))
    if proverka_ydar[3]:
        screen.blit(text_ydar2_2, (415, 10))
        screen.blit(text_sum_ydar2, (400, 60))
    if proverka_ydar[4]:
        screen.blit(text_ydar3, (440, 28))
    if proverka_ydar[5]:
        screen.blit(text_ydar3_2, (455, 10))
        screen.blit(text_sum_ydar3, (440, 60))
    if proverka_ydar[6]:
        screen.blit(text_ydar4, (480, 28))
    if proverka_ydar[7]:
        screen.blit(text_ydar4_2, (495, 10))
        screen.blit(text_sum_ydar4, (480, 60))
    if proverka_ydar[8]:
        screen.blit(text_ydar5, (520, 28))
    if proverka_ydar[9]:
        screen.blit(text_ydar5_2, (535, 10))
        screen.blit(text_sum_ydar5, (520, 60))
    if proverka_ydar[10]:
        screen.blit(text_ydar6, (560, 28))
    if proverka_ydar[11]:
        screen.blit(text_ydar6_2, (575, 10))
        screen.blit(text_sum_ydar6, (560, 60))


text_ydar1 = text_ydar2 = text_ydar3 = text_ydar4 = text_ydar5 = text_ydar6 = text_ydar1_2 = text_ydar2_2 = \
    text_ydar3_2 = text_ydar4_2 = text_ydar5_2 = text_ydar6_2 = ""
text_sum_ydar1 = text_sum_ydar2 = text_sum_ydar3 = text_sum_ydar4 = text_sum_ydar5 = text_sum_ydar6 = ""
ostatok = 0
# оснвоной цикл
if __name__ == '__main__':
    # создание экрана
    start_screen()
    pygame.init()
    size = 900, 630
    screen = pygame.display.set_mode(size)

    all_sprites = pygame.sprite.Group()
    pin_group = pygame.sprite.Group()
    # координаты кегль
    coord_x = [425, 440, 455, 470, 432.5, 446.5, 462.5, 440.5, 455.5, 448]
    coord_y = [110, 110, 110, 110, 120, 120, 120, 130, 130, 140]
    # отрисовка кегль
    for i in range(10):
        Pin(pin_group, coord_x[i], coord_y[i])
    fon = Bowl(all_sprites, 0, 0)
    all_sprites.add(fon)

    shar_group = pygame.sprite.Group()
    im = load_image("ba1ll30-fotor-bg-remover-2025011522518.png")
    orig_im = load_image("ba1ll30-fotor-bg-remover-2025011522518.png")
    im = pygame.transform.scale(orig_im, (40, 40))
    sprite_shar = pygame.sprite.Sprite()
    sprite_shar.image = im
    sprite_shar.rect = sprite_shar.image.get_rect()
    sprite_shar.rect.x = 435
    sprite_shar.rect.y = 400
    shar_group.add(sprite_shar)
    pin_group_spisok = []
    for i in pin_group:
        pin_group_spisok.append(i)

    running = True

    clock = pygame.time.Clock()
    text_in_button = "Start Game"
    x = 200
    y = 400
    r = 0
    numbet_udar = 1
    click = False
    a = False
    h = 0
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    timer = 0
    startTime = time.time()
    # сила удара
    slider = Slider(screen, 350, 480, 200, 20, min=0.1, max=2, step=0.1)
    # вращение шара
    slider_x = Slider(screen, 610, 400, 20, 150, min=0.5, max=1.5, step=0.1, vertical=True)

    plus = True
    slid = True
    proverka_ydar = [False, False, False, False, False, False, False, False, False, False, False, False]
    round = 1
    sum_total = 0
    while running:
        col = 0
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT and click:
                timer += 1
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                # движение шара влево
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and sprite_shar.rect.y == 400 and (
                        sprite_shar.rect.x >= 370 and sprite_shar.rect.x <= 505):
                    sprite_shar.rect.x -= 10
                # движение шара вправо
                elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and sprite_shar.rect.y == 400 and (
                        sprite_shar.rect.x >= 370 and sprite_shar.rect.x <= 505):
                    sprite_shar.rect.x += 10
                # что бы шар не укатилься за пределы
                if sprite_shar.rect.x >= 505:
                    sprite_shar.rect.x = 500
                elif sprite_shar.rect.x <= 375:
                    sprite_shar.rect.x = 370
            if event.type == pygame.MOUSEBUTTONDOWN:
                # нажатие на кнопку start game
                if draw_button("").collidepoint(
                        event.pos) and text_in_button == "Start Game" and a == False and numbet_udar <= 2:
                    text_in_button = "Вернуть Шар"
                    a = True
                    slid = False
                    timer = 0
                    numbet_udar += 1
                    click = True
                    sprite_shar.rect.y = 400
                    x = 200
                if draw_button("").collidepoint(
                        event.pos) and text_in_button == "Вернуть Шар" and a == False and numbet_udar <= 2:
                    click = True
                    timer = 0
                    slid = True
                    sprite_shar.rect.y = 400
                    text_in_button = "Start Game"
                # если последний удар(2)
                elif numbet_udar == 3 and a == False:
                    timer = 0
                    round += 1
                    slid = True
                    sum_total += 10 - len(pin_group)
                    text_in_button = "Start Game"
                    numbet_udar = 1
                    sprite_shar.rect.y = 400
                    if round == 7:
                        round = 1
                        ydar1 = ""
                        ydar2 = ""
                        ydar3 = ""
                        ydar4 = ""
                        ydar5 = ""
                        ydar1_2 = ""
                        ydar2_2 = ""
                        ydar3_2 = ""
                        ydar4_2 = ""
                        ydar5_2 = ""
                        ydar6_2 = ""
                        sum_total = 0
                        proverka_ydar = [False, False, False, False, False, False, False, False, False, False, False,
                                         False]
                    for i in pin_group:
                        col += 1
                    print(f"Вы сбили {10 - col} кеглей")
                    for i in pin_group_spisok:
                        pin_group.add(i)
                    pin_group.draw(screen)
        # отрисовка спрайтов
        all_sprites.draw(screen)
        pin_group.draw(screen)
        shar_group.draw(screen)
        first = True
        clock = pygame.time.Clock()
        # управление слайдером
        if slid:
            if slider_x.value <= 1.5:
                if plus:
                    slider_x.setValue(slider_x.value + 0.01)
            else:
                plus = False
            if slider_x.value >= 0.5:
                if not plus:
                    slider_x.setValue(slider_x.value - 0.01)
            else:
                plus = True

        if click:
            # проверка на старайк
            if not pin_group and numbet_udar == 2:
                numbet_udar += 1
                print("Страйк!!")
            time = pygame.time.get_ticks() / 100
            if a:
                # если кнопка была нажата
                y -= 1
                sprite_shar.rect.y -= 1 + slider.value
                for i in range(0, 10):
                    # удаление кегль
                    if pygame.sprite.collide_mask(pin_group_spisok[i], sprite_shar):
                        pin_group_spisok[i].kill()
                # Дейтсвия что бы шар не укатилься
                if sprite_shar.rect.y % 10 == 0 and sprite_shar.rect.x <= 370:
                    sprite_shar.rect.x += timer * 4
                elif sprite_shar.rect.y % 10 == 0 and sprite_shar.rect.x >= 480:
                    sprite_shar.rect.x -= timer * 4
                if sprite_shar.rect.y % 10 == 0 and slider_x.value <= 1:
                    sprite_shar.rect.x -= slider_x.value
                elif sprite_shar.rect.y % 10 == 0 and slider_x.value >= 1:
                    sprite_shar.rect.x += slider_x.value
        # если шар доехал до конца
        if sprite_shar.rect.y <= 110:
            click = False
            timer = 0
            a = False

        # output.setText(slider.getValue())
        events = pygame.event.get()

        if not a:
            pygame_widgets.update(events)
        # отрисовка таблицы
        Draw_tabl()
        # рисовка цифр в таблице
        Draw_chifr_tabl(numbet_udar, round, proverka_ydar)
        pygame.display.update()
        clock.tick(150)
    # выход из игры
    pygame.quit()
print("Спасибо за игру!")
