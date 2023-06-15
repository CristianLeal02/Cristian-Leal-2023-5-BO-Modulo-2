import pygame, random
from pygame.sprite import Sprite
from game.utils.constants import ENEMY_1, ENEMY_2, SCREEN_HEIGHT, SCREEN_WIDTH, IMAGE_SIZE, SPEED_X_ENEMY

class Enemy(Sprite):
    
    def __init__(self, rect_x):
        self.type_enemy = random.randint(1,3) # esta variable dara un enemigo aleatorio entre el tipo 1 o 2
        self.rect_x = rect_x
        self.select_enemy(self.type_enemy)
        self.speed_y_1 = random.randint(2,5)
        self.speed_y_2 = random.randint(4,8)
        self.count = 0

    def update(self, spaceship):
        self.select_move(self.type_enemy, spaceship)
        self.control_out_screen()
        self.respawn_enemy()

    def select_enemy(self, type_enemy): # selecciona el tipo de enemigo, sea 1 o 2 segun la variable
        if type_enemy <= 2:
            self.image = pygame.transform.scale(ENEMY_1, IMAGE_SIZE)
            self.image_rect = self.image.get_rect()
            self.image_rect.x = self.rect_x
            self.image_rect.y = 0
        else:
            self.image = pygame.transform.scale(ENEMY_2, IMAGE_SIZE)
            self.image_rect = self.image.get_rect()
            self.image_rect.x = self.rect_x
            self.image_rect.y = 0

    def select_move(self, type_enemy, spaceship): # selecciona el tipo de movimiento segun el tipo de enemigo
        if type_enemy <= 2:
            self.image_rect.y += self.speed_y_1
            self.move_1()
            self.image_rect.x
        else:
            self.image_rect.y += self.speed_y_2
            self.move_2(spaceship)

    def move_1(self): # movimiento del enemigo 1
      self.count += 1
      if self.count <= 30:
          self.image_rect.x -= SPEED_X_ENEMY[0]
      elif self.count < 60:
          self.image_rect.x += SPEED_X_ENEMY[0]
      else:
          self.image_rect.x += SPEED_X_ENEMY[0]
          self.count = 0

    def move_2(self, spaceship): # movimiento del enemigo 2
        if spaceship > self.image_rect.x:
            self.image_rect.x += SPEED_X_ENEMY[1]
        else:
            self.image_rect.x -= SPEED_X_ENEMY[1]

    def control_out_screen(self): # evitar que salga de la pantalla 
        if self.image_rect.x > SCREEN_WIDTH - IMAGE_SIZE[0]:
            self.image_rect.x = 0
        elif self.image_rect.x < 0:
            self.image_rect.x = SCREEN_WIDTH - IMAGE_SIZE[0]

    def respawn_enemy(self): # reaparecer el enemigo si este no muere
        if self.image_rect.y > SCREEN_HEIGHT:
            self.image_rect.y = 0
            if self.type_enemy <= 2:
                self.image_rect.x = random.randint(0,SCREEN_WIDTH)