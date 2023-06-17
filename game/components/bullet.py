import pygame
from pygame.sprite import Sprite
from game.utils.constants import BULLET, BULLET_ENEMY, SPEED_BULLET, BULLET_SIZE, SCREEN_HEIGHT

class Bullet(Sprite):
    
    def __init__(self, ship_type, rect_x, rect_y, flag):
        super().__init__()
        self.flag = flag
        self.shoot_type(ship_type)
        self.ship_type = ship_type
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y

    def shoot_type(self, ship_type): # puede implementarse para que los enemigos disparen
        if ship_type == 1:
            self.image = pygame.transform.scale(BULLET, BULLET_SIZE)
        elif ship_type == 2 and self.flag:
            self.image = pygame.transform.scale(BULLET_ENEMY, BULLET_SIZE)

    def update(self):
        self.move_bullet
        if self.ship_type == 1 and self.rect.y < 0:
            self.kill()
        elif self.rect.y < SCREEN_HEIGHT:
            self.kill()

    def move_bullet(self): # movimiento de las balas
        if self.ship_type == 1:
            self.rect.y -= SPEED_BULLET
        else:
            self.rect.y += SPEED_BULLET