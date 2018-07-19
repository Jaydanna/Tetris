import sys
import pygame
from setting import *
from piece import Piece

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Tetris!')

    bg_color = BG_COLOR
    piece = Piece('T',screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill(bg_color)
        draw_game_area(screen)
        piece.paint()
        pygame.display.flip()

def draw_game_area(screen):
    # ##top line
    # pygame.draw.line(screen,EDGE_COLOR,(GAME_AREA_LEFT,GAME_AREA_TOP),
    #                 (GAME_AREA_LEFT+GAME_AREA_WIDTH,GAME_AREA_TOP))
    # ##button line
    # pygame.draw.line(screen,EDGE_COLOR,(GAME_AREA_LEFT,GAME_AREA_HEIGHT+GAME_AREA_TOP),
    #                 (GAME_AREA_LEFT+GAME_AREA_WIDTH,GAME_AREA_HEIGHT+GAME_AREA_TOP)
    # ##left line
    # pygame.draw.line(screen,EDGE_COLOR,(GAME_AREA_LEFT,GAME_AREA_TOP),
    #                 (GAME_AREA_LEFT,GAME_AREA_TOP+GAME_AREA_HEIGHT))
    # ##right line
    # pygame.draw.line(screen,EDGE_COLOR,(GAME_AREA_LEFT+GAME_AREA_WIDTH,GAME_AREA_TOP),
    #                 (GAME_AREA_LEFT+GAME_AREA_WIDTH,GAME_AREA_TOP+GAME_AREA_HEIGHT))

    for r in range(21):
        pygame.draw.line(screen,EDGE_COLOR,(GAME_AREA_LEFT,GAME_AREA_TOP + r*CELL_WIDTH),(GAME_AREA_LEFT+GAME_AREA_WIDTH,GAME_AREA_TOP + r * CELL_WIDTH))

    for c in range(11):
        pygame.draw.line(screen,EDGE_COLOR,(GAME_AREA_LEFT + c*CELL_WIDTH,GAME_AREA_TOP),(GAME_AREA_LEFT + c*CELL_WIDTH,GAME_AREA_TOP+GAME_AREA_HEIGHT))


if __name__=='__main__':
    main()