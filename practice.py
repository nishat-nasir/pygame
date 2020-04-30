import pygame
screen = pygame.display.set_mode((1000, 500))
bg = pygame.image.load('background.png')
mm = pygame.image.load('main_menu.png')
true = True
while true:

    for event in pygame.event.get():
        screen.blit(bg, (0, 0))
        if event.type == pygame.KEYDOWN:
            if event.key != pygame.K_LEFT:
                screen.blit(mm, (0, 0))
        else:
            pass




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            true = False
        # process events


    # Update your sprites
        pygame.display.update()
