from board import Board
from cell import Cell
from menu import *
import pygame, sys
from constants import *
from sudoku_generator import SudokuGenerator


def main():

    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    screen.fill(BG_COLOR)
    board_object = Board(1, 1, screen, difficulty=30)

    board_object.draw()
    pygame.display.update()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    board_object.place_number(4)
                if event.key == pygame.K_5:
                    board_object.sketch(5)
            if event.type == pygame.MOUSEBUTTONDOWN:
                (x, y) = event.pos
                board_object.click(x, y)
                board_object.sketch(5)

    # board_object.sketch(8)


main()
