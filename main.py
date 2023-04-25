import pygame, sys

pygame.init()
pygame.display.set_caption("BITCH ASS SUDOKU")
screen = pygame.display.set_mode((600, 600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()