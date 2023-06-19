import pygame
from pygame.sprite import Sprite
from game.utils.constants import GAME_OVER, GAME_OVER_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, ALL_SPRITES

class Game_over(Sprite):
    
    def __init__(self, screen):
        super().__init__()
        self.image = pygame.transform.scale(GAME_OVER, GAME_OVER_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2.2)
        ALL_SPRITES.empty()