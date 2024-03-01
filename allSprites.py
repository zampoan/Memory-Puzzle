import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect((0, 0, 80, 80))
        self.color = color

        self.coverImage = pygame.Surface(self.rect.size)
        self.coverImage.fill('grey')

        self.hoverImage = pygame.Surface(self.rect.size)
        self.hoverImage.fill('light grey')

        self.revealedImage = pygame.Surface(self.rect.size)
        self.revealedImage.fill(color, self.rect.inflate(-10, -10))

        self.image = self.coverImage

        self.revealed = False
        self.solved = False

        self.rect.topleft = (x, y)

    def toggle(self):
        """
        Makes solved tiles appear permanently visible
        """
        if not self.solved:
            self.revealed = not self.revealed

    def update(self, mousepos):
        # Hovering
        if self.rect.collidepoint(mousepos):
            self.image = self.hoverImage
        else:
            self.image = self.coverImage
        
        # Revealing
        if self.revealed:
            self.image = self.revealedImage
        else:
            self.image = self.coverImage
