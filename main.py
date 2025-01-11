import os
import sys
import pygame
import random


def load_image(name, colorkey=None):
    screen = pygame.display.set_mode((500, 500))
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
    image = load_image("ba1ll30.png")

    def __init__(self, group, x, y):
        super().__init__(group)
        self.image2 = Bowl.image
        self.rect = self.image2.get_rect()

        self.image2 = pygame.transform.scale(self.image2, (0, 0))
        self.rect.topleft = (x, y)


class Bowl(pygame.sprite.Sprite):
    image = load_image("fon.png")
    pin_image = load_image("kegl.png")


    def __init__(self, group, x, y):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно !!!
        # размер окна у меня 500 на 500
        super().__init__(group)
        self.image = Bowl.image
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (500, 500))
        self.rect.topleft = (x, y)


        self.velocity = random.randint(1, 5)
        self.xx = 200
        self.yy = 400


        self.r = 0


    def update(self, *args):
        time = clock.tick() / 1000


        r = 0


        if self.yy >= 70:
            self.yy -= 1
            self.xx += 0.101
        Shar(pin_group, self.xx, self.yy)
        print(pygame.sprite.groupcollide(pin_group, shar_group, False, False))

        return self.yy



def draw_button():
    # print("sda")
    font = pygame.font.Font(None, 24)
    button_surface = pygame.Surface((150, 50))
    text = font.render("Click Me", True, (255, 255, 255))
    text_rect = text.get_rect(
        center=(button_surface.get_width() / 2,
                button_surface.get_height() / 2))
    button_rect = pygame.Rect(160, 450, 150, 50)
    screen.blit(button_surface, (button_rect.x, button_rect.y))
    return button_rect


if __name__ == '__main__':
    pygame.init()
    size = 500, 500
    screen = pygame.display.set_mode(size)
    screen.fill((255, 255, 255))

    all_sprites = pygame.sprite.Group()
    fon = Bowl(all_sprites, 0, 0)
    print(fon)
    all_sprites.add(fon)

    pin_group = pygame.sprite.Group()
    pin7 = Pin(pin_group, 225, 25)
    pin8 = Pin(pin_group, 240, 25)
    pin9 = Pin(pin_group, 255, 25)
    pin10 = Pin(pin_group, 270, 25)
    pin4 = Pin(pin_group, 232.5, 35)
    pin5 = Pin(pin_group, 246.5, 35)
    pin6 = Pin(pin_group, 262.5, 35)
    pin2 = Pin(pin_group, 240.5, 45)
    pin3 = Pin(pin_group, 255.5, 45)
    pin1 = Pin(pin_group, 247, 55)





    pin_group.add(pin7)
    pin_group.add(pin8)
    pin_group.add(pin9)
    pin_group.add(pin10)
    pin_group.add(pin4)
    pin_group.add(pin5)
    pin_group.add(pin6)
    pin_group.add(pin2)
    pin_group.add(pin3)
    pin_group.add(pin1)

    shar_group = pygame.sprite.Group()
    shar = Shar(pin_group, 200, 400)
    shar_group.add(shar)

    running = True

    clock = pygame.time.Clock()
    x = 200
    y = 400
    r = 0
    click = False
    while running:
        time = clock.tick() / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # for bomb in all_sprites:
                #     all_sprites.update(event)
                if draw_button().collidepoint(event.pos):
                    print("213333333333")
                    click = True


        r += 500 * time


        all_sprites.draw(screen)
        pin_group.draw(screen)
        if click:
            all_sprites.update(event)
        draw_button()

        # butt = Bowl(all_sprites, 0, 0)
        # butt.draw_button()

        # button_surface.blit(text, text_rect)
        # screen.blit(button_surface, (button_rect.x, button_rect.y))
        # pygame.draw.circle(screen, (255, 255, 255), (x, y), 12)
        pygame.display.flip()
        clock.tick(155)

    pygame.quit()
