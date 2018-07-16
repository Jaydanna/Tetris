import sys
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((1200, 900))
    pygame.display.set_caption('Tetris!')

    bg_color = (230,230,230)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill(bg_color)
        pygame.display.flip()

def draw_game_area(screen):
    pygame.draw.line(screen,(0,0,0),(100,100),(200,200))

if __name__=='__main__':
    main()