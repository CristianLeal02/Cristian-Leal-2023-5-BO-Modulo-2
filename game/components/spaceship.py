import pygame
from pygame.sprite import Sprite
from game.components.bullet import Bullet
from game.utils.constants import SPACESHIP, SCREEN_HEIGHT, SCREEN_WIDTH, SPEED, IMAGE_SIZE, ALL_SPRITES, GROUP_BULLETS

class SpaceShip(Sprite):
    
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(SPACESHIP, IMAGE_SIZE)
        self.rect = self.image.get_rect()
        self.rect.x = (SCREEN_WIDTH / 2) - (IMAGE_SIZE[0] / 2)
        self.rect.y = SCREEN_HEIGHT - IMAGE_SIZE[1] - 20
        self.bullets = []
        self.count_updates = 0

    def update(self):
        self.control_out_screen()
        self.shoot_bullet()
        for i in self.bullets:
            i.move_bullet()

    def move(self): # movimiento de la nave izquierda y derecha
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += SPEED
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= SPEED

    def control_out_screen(self): # evitar que salga de la pantalla transportando al lado opuesto
        if self.rect.x > SCREEN_WIDTH - IMAGE_SIZE[0]:
            self.rect.x = 0
        elif self.rect.x < 0:
            self.rect.x = SCREEN_WIDTH - IMAGE_SIZE[0]

    def shoot_bullet(self): # genera disparo
        keys = pygame.key.get_pressed()
        self.count_updates += 1
        if keys[pygame.K_SPACE] and self.count_updates >= 10 and self.alive():
            point_x = self.rect.x + (IMAGE_SIZE[0] / 2.7)
            bullet = Bullet(1, point_x, (SCREEN_HEIGHT - IMAGE_SIZE[1] - 20), None)
            self.bullets.append(bullet)
            self.count_updates = 0
            GROUP_BULLETS.add(bullet)
            ALL_SPRITES.add(bullet)