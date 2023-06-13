import pygame
from pygame.sprite import Sprite

from game.utils.constants import SPACESHIP, SCREEN_HEIGHT, SCREEN_WIDTH, SPEED

# casi Todo en pygame es un objeto
# Un personaje en mi juego es un objeto (instancia de algo)
# La nave (spaceship) es un personaje => necesito una clase


# SpaceShip es una clase derivada (hija) de Sprite

# spaceship tiene una "imagen"
class SpaceShip(Sprite):
    
    def __init__(self):
        self.image_size = (40, 60)
        self.image = pygame.transform.scale(SPACESHIP, self.image_size)
        self.image_rect = self.image.get_rect()
        self.image_rect.x = (SCREEN_WIDTH / 2) - (self.image_size[0] / 2)
        self.image_rect.y = SCREEN_HEIGHT - self.image_size[1] - 20

    def update(self):
        self.move()
        self.control_out_screen()

    def move(self): # movimiento de la nave izquierda y derecha
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.image_rect.x += SPEED
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.image_rect.x -= SPEED

    def control_out_screen(self): # evitar que salga de la pantalla transportando al lado opuesto
        if self.image_rect.x > SCREEN_WIDTH - self.image_size[0]:
            self.image_rect.x = 0
        elif self.image_rect.x < 0:
            self.image_rect.x = SCREEN_WIDTH - self.image_size[0]




