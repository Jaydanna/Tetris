import sys
import pygame

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900
CELL_WIDTH = 40
GAME_AREA_WIDTH = CELL_WIDTH * 10
GAME_AREA_HEIGHT = CELL_WIDTH * 20
GAME_AREA_LEFT = (SCREEN_WIDTH - GAME_AREA_WIDTH) // 2
GAME_AREA_TOP = SCREEN_HEIGHT - GAME_AREA_HEIGHT
EDGE_COLOR = (0,0,0)
CELL_COLOR = (100,100,100)
BG_COLOR = (230,230,230)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Tetris!')

    bg_color = BG_COLOR

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill(bg_color)
        draw_game_area(screen)
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
        pygame.draw.line(screen.EDGE_COLOR,(GAME_AREA_LEFT + c*CELL_WIDTH,GAME_AREA_TOP),(GAME_AREA_LEFT + c*CELL_WIDTH,GAME_AREA_TOP+GAME_AREA_HEIGHT))

if __name__=='__main__':
    main()