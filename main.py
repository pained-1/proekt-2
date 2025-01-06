import os
import sys
import pygame
import random


def load_image(name, colorkey=None):
    screen = pygame.display.set_mode((1900, 1000))
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


class Bowl(pygame.sprite.Sprite):
    image = load_image("fon1.png")

    # image_boom = load_image("boom.png")
    # fon = load_image("fon1.png")

    def __init__(self, group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно !!!
        #размер окна у меня 500 на 500
        super().__init__(group)
        # self.image = Bowl.image
        self.image = Bowl.image
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (500, 500))
        # pygame.transform.scale(self.image, (600, 600))
        # print(self.image.get_size())
        # self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        # self.rect.x = 0
        # self.rect.y = 0

    def update(self, *args):
        pass
        # self.image = self.fon
        # self.rect = self.rect.move(random.randrange(3) - 1,
        #                            random.randrange(3) - 1)
        # self.rect1 = self.rect1.move(random.randrange(3) - 1,
        #                            random.randrange(3) - 1)


if __name__ == '__main__':
    pygame.init()
    size = 500, 500
    screen = pygame.display.set_mode(size)
    screen.fill((255, 255, 255))
    all_sprites = pygame.sprite.Group()
    Bowl(all_sprites)
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for bomb in all_sprites:
                    all_sprites.update(event)
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(155)

    pygame.quit()
