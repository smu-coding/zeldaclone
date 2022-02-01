import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
      super().__init__(groups)
      self.image = pygame.image.load('zeldaclone/assets/player.png').convert_alpha()
      self.rect = self.image.get_rect(topleft = pos)

      self.direction = pygame.math.Vector2()
    
    def input(self):
        keys = pygame.key.get_pressed()