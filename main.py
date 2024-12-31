import pygame
from player import player1, player2

pygame.init()

size = (600, 500)
window = pygame.display.set_mode(size)
pygame.display.set_caption('Догонялки')

FPS = 60
clock = pygame.time.Clock()

bg = pygame.image.load('bg.png')
bg = pygame.transform.scale(bg, size)


game = True
while game:
    window.blit(bg, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    player1.move(size, 'wasd')
    player1.draw(window)

    player2.move(size, 'arrows')
    player2.draw(window)

    clock.tick(FPS)
    pygame.display.flip()