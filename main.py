import pygame
from allSprites import Tile
import random

SCREEN_HEIGHT = 550
SCREEN_WIDTH = 600
NUM_COLS = 4
NUM_ROWS = 4
COLORS = ['red','blue', 'green', 'yellow', 'darkviolet', 'deeppink', 'aqua', 'orange']


def resetGameState(sprites):
    sprites.empty()
    
    pool = []
    for c in COLORS:
        pool.append(c)
        pool.append(c)

    random.shuffle(pool)

    for i in range(1, NUM_COLS + 1):
        for j in range(1, NUM_ROWS + 1):
            sprites.add(Tile(100 * i, 100 * j, pool.pop()))


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    sprites = pygame.sprite.Group()

    font = pygame.font.Font(None, 32)

    resetGameState(sprites)

    running = True
    totalMoves = 0
    
    # Keep track of selected tiles
    selected = []

    while running:
        mousepos = pygame.mouse.get_pos()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN and pygame.K_ESCAPE:
                resetGameState(sprites)
                totalMoves = 0 

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # two unmatched tiles revealed
                if len(selected) == 2:
                    selected[0].toggle()
                    selected[1].toggle()
                    selected.clear()
                else:
                    for s in sprites:
                        
                        # click on non-solved tile to reveal
                        if s.rect.collidepoint(event.pos):
                            # Increment moves only on revealed tiles
                            if s.revealed == False:
                                totalMoves += 1
                            s.revealed = True
                            selected.append(s)


                        # click on two tiles which are same color, set to solved and clear the arr
                        if len(selected) == 2 and selected[0].color == selected[1].color:
                            selected[0].solved = True
                            selected[1].solved = True
                            selected.clear()

        screen.fill('black')

        scoreText = font.render(f'Total Moves: {totalMoves}', True, 'white')
        screen.blit(scoreText, (10, 10))

        sprites.update(mousepos)
        sprites.draw(screen)

        pygame.display.flip()

    pygame.quit()

if __name__=="__main__":
    main()