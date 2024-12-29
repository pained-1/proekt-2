#ТЕСТ РАБОТОСПОСОБНОСТИ

import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('боулинг')
    size = width, height = 1000,1000
    screen = pygame.display.set_mode(size)

    fps = 144 # количество кадров в секунду
    clock = pygame.time.Clock()
    running = True
    moving = False
    x, y = 0, 0
    rect = pygame.draw.rect(screen, (0, 0, 0), (0, 0, 100, 100), 0)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if rect.collidepoint(event.pos):
                    moving = True
            elif event.type == pygame.MOUSEBUTTONUP:
                moving = False
            elif event.type == pygame.MOUSEMOTION and moving:
                x_new, y_new = event.rel
                x, y = x + x_new, y + y_new
                rect.move_ip(event.rel)
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (0, 255, 0), (x, y, 100, 100))
        pygame.display.flip()
        clock.tick(fps)
