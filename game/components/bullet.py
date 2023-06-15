import pygame
from pygame.sprite import Sprite

from game.utils.constants import BULLET, BULLET_ENEMY, SCREEN_HEIGHT, SCREEN_WIDTH, SPEED_BULLET, BULLET_SIZE

# casi Todo en pygame es un objeto
# Un personaje en mi juego es un objeto (instancia de algo)
# La nave (spaceship) es un personaje => necesito una clase


# SpaceShip es una clase derivada (hija) de Sprite

# spaceship tiene una "imagen"
class Bullet(Sprite):
    
    def __init__(self, ship_type, rect_x, rect_y):
        super().__init__()
        self.shoot_type(ship_type)
        self.ship_type = ship_type
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y

    def shoot_type(self, ship_type):
        if ship_type == 1:
            self.image = pygame.transform.scale(BULLET, BULLET_SIZE)
        else:
            self.image = pygame.transform.scale(BULLET_ENEMY, BULLET_SIZE)

    def move_bullet(self):
        if self.ship_type == 1:
            self.rect.y -= SPEED_BULLET
        else:
            self.rect.y += SPEED_BULLET

    def deat(self):
        self.kill()