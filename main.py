import os
import sys
import pygame
import random
from decimal import *


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


class Pin(pygame.sprite.Sprite):
    image = load_image("kegl.png")

    def __init__(self, group, x, y):
        super().__init__(group)
        self.image1 = Bowl.image
        self.rect = self.image1.get_rect()
        self.image1 = pygame.transform.scale(self.image1, (0, 0))
        self.rect.topleft = (x, y)


class Shar(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (200, 300)

        # self.image2 = pygame.transform.scale(self.image2, (0, 0))

    # def draw(self,x,y):
    #     screen = pygame.display.set_mode((500, 500))
    #     print(self.image2)
    #     screen.blit(self.image2, (self.x, self.y))


class Bowl(pygame.sprite.Sprite):
    image = load_image("1free-bowling-alley-background-vector.png")
    pin_image = load_image("kegl.png")

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

    def update(self, *args):
        time = clock.tick() / 1000

        r = 0

        # if self.yy >= 70:
        #     self.yy -= 1
        #
        #     self.xx += 0.101
        # Shar(pin_group, self.xx, self.yy)

        # print(pygame.sprite.groupcollide(pin_group, shar_group, False, False))

        return self.yy


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


if __name__ == '__main__':
    pygame.init()
    size = 900, 630
    screen = pygame.display.set_mode(size)
    screen.fill((255, 255, 255))

    all_sprites = pygame.sprite.Group()
    fon = Bowl(all_sprites, 0, 0)
    all_sprites.add(fon)

    pin_group = pygame.sprite.Group()
    pin7 = Pin(pin_group, 425, 110)
    pin8 = Pin(pin_group, 440, 110)
    pin9 = Pin(pin_group, 455, 110)
    pin10 = Pin(pin_group, 470, 110)
    pin4 = Pin(pin_group, 432.5, 120)
    pin5 = Pin(pin_group, 446.5, 120)
    pin6 = Pin(pin_group, 462.5, 120)
    pin2 = Pin(pin_group, 440.5, 130)
    pin3 = Pin(pin_group, 455.5, 130)
    pin1 = Pin(pin_group, 448, 140)

    # pin_group.add(pin7)
    # pin_group.add(pin8)
    # pin_group.add(pin9)
    # pin_group.add(pin10)
    # pin_group.add(pin4)
    # pin_group.add(pin5)
    # pin_group.add(pin6)
    # pin_group.add(pin2)
    # pin_group.add(pin3)
    # pin_group.add(pin1)

    # shar_group = pygame.sprite.Sprite(all_sprites)
    shar_group = pygame.sprite.Group()
    im = load_image("ba1ll30-fotor-bg-remover-2025011522518.png")
    sprite_shar = pygame.sprite.Sprite()
    # shar_group.image = im
    sprite_shar.image = im
    # shar_group.rect = shar_group.image.get_rect()
    # shar_group.rect.top = 400
    # shar_group.rect.right = 250
    sprite_shar.rect = sprite_shar.image.get_rect()
    sprite_shar.rect.x = 435
    sprite_shar.rect.y = 400
    shar_group.add(sprite_shar)
    pin_group_spisok = []
    for i in pin_group:
        pin_group_spisok.append(i)

    # all_sprites.add(shar_group)

    # shar_group.add(Shar(pin_group, 200, 400))

    running = True

    clock = pygame.time.Clock()
    text_in_button = "Start Game"
    x = 200
    y = 400
    r = 0
    numbet_udar = 1
    click = False
    a = False
    while running:
        time = clock.tick() / 1000
        col = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and sprite_shar.rect.y == 400:
                    sprite_shar.rect.x -= 10
                elif event.key == pygame.K_RIGHT and sprite_shar.rect.y == 400:
                    sprite_shar.rect.x += 10
            if event.type == pygame.MOUSEBUTTONDOWN:
                if draw_button("").collidepoint(
                        event.pos) and text_in_button == "Start Game" and a == False and numbet_udar <= 2:
                    text_in_button = "Вернуть Шар"
                    a = True
                    numbet_udar += 1
                    click = True
                    sprite_shar.rect.y = 400
                    x = 200
                if draw_button("").collidepoint(
                        event.pos) and text_in_button == "Вернуть Шар" and a == False and numbet_udar <= 2:
                    click = True
                    sprite_shar.rect.y = 400
                    text_in_button = "Start Game"
                elif numbet_udar == 3 and a == False:
                    text_in_button = "Start Game"
                    numbet_udar = 1
                    sprite_shar.rect.y = 400
                    for i in pin_group:
                        col += 1
                    print(f"Вы сбили {10 - col} кеглей")
                    for i in pin_group_spisok:
                        pin_group.add(i)
                    pin_group.draw(screen)

        r += 500 * time

        all_sprites.draw(screen)
        pin_group.draw(screen)
        shar_group.draw(screen)
        B = False
        first = True

        if click:
            # all_sprites.update(event)\
            h = pygame.sprite.groupcollide(shar_group, pin_group, False, False)
            if a:
                y -= 1
                sprite_shar.rect.y -= 1
                # sprite_shar.rect.x += 1

                # if y >= 70:
                #     y -= 1
                #     x += 0.101
                #     shar_group.rect.y -= 1
                B = False
                # if pygame.sprite.groupcollide(shar_group, pin_group, False,False) and y == 110:
                #     pygame.sprite.groupcollide(shar_group, pin_group, True,True)
                # print(h)
                # sprite_shar.mask = pygame.mask.from_surface(sprite_shar.image)
                for i in range(0, 10):
                    if pygame.sprite.collide_mask(pin_group_spisok[i], sprite_shar):
                        pin_group_spisok[i].kill()

            else:
                B = True

        if sprite_shar.rect.y == 110:
            click = False
            a = False
            # pygame.sprite.groupcollide(shar_group, pin_group, True, True)

            # Shar.draw(x, y)
            # Shar(pin_group, x, y)
            # shar_group.draw(screen)

        draw_button(text_in_button)

        # butt = Bowl(all_sprites, 0, 0)
        # butt.draw_button()

        # button_surface.blit(text, text_rect)
        # screen.blit(button_surface, (button_rect.x, button_rect.y))
        # pygame.draw.circle(screen, (255, 255, 255), (x, y), 12)
        # pygame.display.flip()
        pygame.display.update()
        clock.tick(155)

    pygame.quit()
