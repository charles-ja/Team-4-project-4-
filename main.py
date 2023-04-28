from sudoku_generator import SudokuGenerator
from menu import *
import pygame, sys
from constants import *


def main():

    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    dif = 0

    while dif == 0:
        pygame.display.set_caption("Sudoku")

        # image upload
        image = pygame.image.load("Sudoku.png")

        # Initialize title font
        start_title_font = pygame.font.Font(None, 70)
        button_font = pygame.font.Font(None, 50)

        screen.blit(image, (0, 0))

        # Initialize and draw title
        title_surface = start_title_font.render(" Sudoku ", True, MAROON, NAVY)
        title_rectangle = title_surface.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 - 150))
        screen.blit(title_surface, title_rectangle)

        # Initialize buttons
        Dif_1 = button_font.render("Easy", True, MAROON, BLACK)
        Dif_2 = button_font.render("Medium", True, MAROON, BLACK)
        Dif_3 = button_font.render("Hard", True, MAROON, BLACK)

        Dif_1_rec = Dif_1.get_rect()
        Dif_2_rec = Dif_2.get_rect()
        Dif_3_rec = Dif_3.get_rect()

        Dif_1_rec.center = (100, 500)
        Dif_2_rec.center = (300, 500)
        Dif_3_rec.center = (500, 500)

        screen.blit(Dif_1, Dif_1_rec)
        screen.blit(Dif_2, Dif_2_rec)
        screen.blit(Dif_3, Dif_3_rec)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Dif_1_rec.collidepoint(event.pos):
                    dif = 30

                elif Dif_2_rec.collidepoint(event.pos):
                    dif = 40

                elif Dif_3_rec.collidepoint(event.pos):
                    dif = 50

    screen.fill(BG_COLOR)
    board_object = Board(1, 1, screen, dif)
    sudoku_object = SudokuGenerator(9, dif)
    board_object.draw()
    pygame.display.update()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                (x, y) = event.pos
                board_object.click(x, y)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    board_object.clear()
                    board_object.click(x, y)
            if board_object.value != 0 and event.type == pygame.KEYDOWN:
                if 48 < event.key < 58:
                    board_object.sketch_white(board_object.value)
                    board_object.place_white(board_object.value)
                    visual = int(chr(event.key))
                    board_object.sketch(visual)
                    board_object.value = visual
            if event.type == pygame.KEYDOWN:
                if 48 < event.key < 58:
                    visual = int(chr(event.key))
                    print(board_object.value)
                    board_object.sketch(visual)
                    board_object.value = visual
                    print(board_object.value)
                if event.key == 13:
                    board_object.sketch_white(visual)
                    board_object.place_number(visual)
                    board_object.board[board_object.row][board_object.col] = visual
                if event.key == pygame.K_BACKSPACE:
                    board_object.board[board_object.row][board_object.col] = 0
                    board_object.sketch_white(visual)
                    board_object.place_white(visual)
                    board_object.draw()
            if board_object.is_full():
                for i in range(len(board_object.board)):
                    if board_object.board[i].is_valid():
                        won = True
                won = False
                if won is True:
                    draw_game_over(screen, True)
                if won is False:
                    draw_game_over(screen, False)


main()
