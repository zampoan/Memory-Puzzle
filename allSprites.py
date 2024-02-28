import pygame

class CoverBox(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.width = 80
        self.height = 80
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill('grey')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.visible = True
        self.paired = False # when self.paired is True, self.visible stays False always
        self.notVisibleCounter = 0

    def toggleVisible(self):
        self.visible = not self.visible

    def draw(self, surface):
        if self.visible:
            surface.blit(self.image, self.rect)
        

class Circle(pygame.sprite.Sprite):
    def __init__(self, x, y, color) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.width = 50
        self.height = 50
        self.image = pygame.Surface([self.width, self.height])
        self.color = color
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y