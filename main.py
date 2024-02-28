import pygame
from allSprites import CoverBox, Circle
import random

SCREEN_HEIGHT = 550
SCREEN_WIDTH = 600
NUM_COLS = 4
NUM_ROWS = 4
COLORS = {'red': 0,'blue' :0,
                  'green':0,'yellow':0, 
                  'darkviolet':0,'deeppink':0, 
                  'aqua':0, 'orange':0}

def doSprite():
    coverBoxSpriteList = pygame.sprite.Group()
    circleSpriteList = pygame.sprite.Group()

    for i in range(1, NUM_COLS + 1):
        for j in range(1, NUM_ROWS + 1):
            # Circle Sprites
            choice = random.choice(list(COLORS.keys()))
            if COLORS[choice] < 2:
                COLORS[choice] += 1
                circleSpriteList.add(Circle(100 * i, 100 * j, choice))
            else:
                # Find the key that has lowest value and increment
                minKey = min(COLORS, key=COLORS.get)
                COLORS[minKey] += 1
                circleSpriteList.add(Circle(100 * i, 100 * j, minKey))

            # CoverBox Sprites
            coverBoxSpriteList.add(CoverBox(100 * i, 100 * j))

    return coverBoxSpriteList, circleSpriteList

def gameLoop(screen):
    visibleCounter = 0
    twoColors = []
    running = True


    coverBoxSpriteList, circleSpriteList = doSprite()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for sprite in coverBoxSpriteList:
                        if sprite.rect.collidepoint(event.pos):
                            sprite.toggleVisible()
                            # When coverBoxSprite becomes invisible
                            if sprite.visible == False:
                                # Output: Two of the same colors 
                                for idx_i, sprite_cb in enumerate(coverBoxSpriteList):
                                    if sprite_cb.visible == False:
                                        for idx_j, sprite in enumerate(circleSpriteList):
                                            if idx_i == idx_j:
                                                if visibleCounter == 1:
                                                    twoColors.append(sprite.color)
                                                    if len(twoColors) == 2:
                                                        if twoColors[0] == twoColors[1]:
                                                            sprite_cb.paired = True
                                                            print(twoColors)
                                                        twoColors = []
                                                    
                                visibleCounter += 1
                            else:
                                visibleCounter -= 1
                            
                            if visibleCounter > 2:
                                # Check if there are two sprites of the same color
                                for sprite in coverBoxSpriteList:
                                    if sprite.paired == True:
                                        sprite.visible = False
                                    elif sprite.paired == False:
                                        sprite.visible = True
                                visibleCounter = 0

        screen.fill('black')

        # Sprite Lists
        circleSpriteList.update()
        circleSpriteList.draw(screen)

        coverBoxSpriteList.update()
        for sprite in coverBoxSpriteList:
            sprite.draw(screen)

        mousePos = pygame.mouse.get_pos()

        for sprite in coverBoxSpriteList:
            if sprite.rect.collidepoint(mousePos):
                sprite.image.fill('white')
            else:
                sprite.image.fill('grey')

        pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gameLoop(screen)

    pygame.quit()

if __name__=="__main__":
    main()