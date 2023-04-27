import pygame, sys

pygame.init()
pygame.display.set_caption("BITCH ASS SUDOKU")
screen = pygame.display.set_mode((600, 600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                board_object.place_number(4)
            if event.key == pygame.K_s:
                board_object.sketch(5)
        if event.type == pygame.MOUSEBUTTONDOWN:
            (x, y) = event.pos
            board_object.click(x, y)
    pygame.display.update()
