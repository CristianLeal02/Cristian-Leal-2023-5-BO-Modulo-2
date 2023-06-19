import pygame
from pygame.sprite import Sprite
from game.utils.constants import HEART, HEART_SIZE

class Lives(Sprite):
    
    def __init__(self, rect_x):
        super().__init__()
        self.image = pygame.transform.scale(HEART, HEART_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = (rect_x, 20)