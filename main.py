#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import pygame
import random
import time
from setting import *
from piece import Piece
from GameWall import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Tetris!')

    bg_color = BG_COLOR
    piece = None
    random.seed(int(time.time()))
    piece = Piece(random.choice(PIECE_TYPES),screen)
    game_wall = GameWall(screen)
    while True:
        if not piece or piece.is_on_buttom:
            piece = Piece(random.choice(PIECE_TYPES),screen)
        check_events(piece)
        
        screen.fill(bg_color)
        draw_game_area(screen)
        piece.paint()
        pygame.display.flip()

def check_events(piece):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                print(u'向下方+1')
                # piece.move_down()
                piece.fall_down()
            elif event.key == pygame.K_UP:
                piece.turn()
                print(u'向上方向键被按下')
            elif event.key == pygame.K_RIGHT:
                print(u'向右方向+1')
                piece.move_right()
            elif event.key == pygame.K_LEFT:
                print(u'向左方向-1')
                piece.move_left()
            # elif event.key == pygame.K_f:
            #     print(u'按下f')
            #     piece.fall_down()


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

    for r in range(R_NUM + 1):
        pygame.draw.line(screen,EDGE_COLOR,(GAME_AREA_LEFT,GAME_AREA_TOP + r*CELL_WIDTH),
                        (GAME_AREA_LEFT+GAME_AREA_WIDTH,GAME_AREA_TOP + r * CELL_WIDTH))

    for c in range(C_NUM + 1):
        pygame.draw.line(screen,EDGE_COLOR,(GAME_AREA_LEFT + c*CELL_WIDTH,GAME_AREA_TOP),(GAME_AREA_LEFT + c*CELL_WIDTH,GAME_AREA_TOP+GAME_AREA_HEIGHT))


if __name__=='__main__':
    main()