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
    image = load_image("pin_main.png")

    def __init__(self, group):
        super().__init__(group)
        self.image1 = Bowl.image
        self.rect = self.image1.get_rect()

        self.image1 = pygame.transform.scale(self.image1, (0, 0))
        self.rect.topleft = (215, -20)


class Bowl(pygame.sprite.Sprite):
    image = load_image("fon.png")
    pin_image = load_image("pin.png")
    # image_boom = load_image("boom.png")
    # fon = load_image("fon1.png")

    def __init__(self, group, x, y):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно !!!
        #размер окна у меня 500 на 500
        super().__init__(group)
        self.image = Bowl.image
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (500, 500))
        self.rect.topleft = (x,y)
        self.velocity = random.randint(1,5)
        self.xx = 200
        self.yy = 400


        # self.cirlcle = pygame.draw.circle(screen, (255,255,255), (100, 100), 50)


        # self.x = 200
        # self.y = 400
        # self.r = 0


        # self.image = Bowl.image
        #
        # self.rect = self.image.get_rect()
        # self.image = pygame.transform.scale(self.image, (500, 500))
        # pygame.transform.scale(self.image, (600, 600))

        # print(self.image.get_size())
        # self.rect = self.image.get_rect()
        # self.rect.x = 0
        # self.rect.y = 0
        # self.rect.x = 0
        self.r = 0
        # self.draw_button()
        # self.rect.y = 0

    def update(self, *args):
        time = clock.tick() / 1000
        # self.rect.y += self.velocity
    #     self.image = Bowl.image
    #
    #     self.rect = self.image.get_rect()
    #     self.image = pygame.transform.scale(self.image, (500, 500))
    #     self.image = pygame.transform.scale(self.image, (500, 500))
    #     screen = pygame.display.set_mode((500, 500))
    #     self.rect.x = 0
    #     self.rect.y = 0
    #     self.y -= self.r
    #     self.x += 0.101
    #     self.r += 500 * time

        r = 0
        # r += 500 * time
        if self.yy >= 70:
            self.yy -= 1
            self.xx += 0.101
        pygame.draw.circle(screen, (255, 255, 255), (self.xx, self.yy), 12)
        return self.yy
    #     # self.image = self.fon
    #
    #     # self.rect = self.rect.move(random.randrange(3) - 1,
    #     #                            random.randrange(3) - 1)
    #     # self.rect1 = self.rect1.move(random.randrange(3) - 1,
    #     #                            random.randrange(3) - 1)
    #     self.button_surface.blit(self.text, self.text_rect)
    #     screen.blit(self.button_surface, (self.button_rect.x, self.button_rect.y))
    #     pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), 12)
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
    pin = Pin(pin_group)
    print(pin)
    pin_group.add(pin)

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

                # if button_rect.collidepoint(event.pos):
                #     print("Button clicked!")
                #
                #     y -= r
                #     x += 0.101

        r += 500 * time

        # y -= r
        # x += 0.101

        # screen.fill((0, 0, 0))

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
