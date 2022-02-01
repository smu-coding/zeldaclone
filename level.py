import pygame

class Level:
    def __init__(self):

        ### GET THE DISPLAY SURFACE ###
        self.display_surface = pygame.display.get_surface()
        
        ### SPRITE GROUP SETUP ###
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()
    
    ### UPDATE AND DRAW THE LEVEL ###
    def run(self):
        pass