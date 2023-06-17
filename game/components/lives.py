import pygame
from pygame.sprite import Sprite
from game.utils.constants import HEART, GAME_OVER_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, ALL_SPRITES, BG

class Game_over(Sprite):
    
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(HEART, GAME_OVER_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)