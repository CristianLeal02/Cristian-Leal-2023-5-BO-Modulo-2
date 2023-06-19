import pygame
from pygame.sprite import Sprite
from game.utils.constants import RESET, RESET_SIZE, SCREEN_WIDTH

class Reset_button(Sprite):
    def __init__(self, rect_y):
        super().__init__()
        self.image = pygame.transform.scale(RESET, RESET_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH / 2, rect_y + 120)