import pygame, random
from pygame.sprite import Sprite
from game.components.bullet import Bullet
from game.utils.constants import ENEMY_1, ENEMY_2, SCREEN_HEIGHT, SCREEN_WIDTH, IMAGE_SIZE, SPEED_X_ENEMY, GROUP_BULLETS_ENEMYS, ALL_SPRITES

class Enemy(Sprite):
    
    def __init__(self, rect_x):
        super().__init__()
        self.type_enemy = random.randint(1, 3) # esta variable dara un enemigo aleatorio entre el tipo 1 o 2
        self.rect_x = rect_x
        self.select_enemy(self.type_enemy)
        self.speed_y_1 = random.randint(4, 7)
        self.speed_y_2 = random.randint(6, 10)
        self.count = 0

    def update(self, spaceship):
        self.select_move(self.type_enemy, spaceship)
        self.control_out_screen()
        self.respawn_enemy()

    def select_enemy(self, type_enemy): # selecciona el tipo de enemigo, sea 1 o 2 segun la variable
        if type_enemy <= 2:
            self.image = pygame.transform.scale(ENEMY_1, IMAGE_SIZE)
            self.rect = self.image.get_rect()
            self.rect.x = self.rect_x
            self.rect.y = 0
        else:
            self.image = pygame.transform.scale(ENEMY_2, IMAGE_SIZE)
            self.rect = self.image.get_rect()
            self.rect.x = self.rect_x
            self.rect.y = 0

    def select_move(self, type_enemy, spaceship): # selecciona el tipo de movimiento segun el tipo de enemigo
        if type_enemy <= 2:
            self.rect.y += self.speed_y_1
            self.move_zigzag()
            self.rect.x
        else:
            self.rect.y += self.speed_y_2
            self.move_chasing(spaceship)

    def move_zigzag(self): # movimiento del enemigo 1
        self.count += 1
        if self.count <= 30:
            self.rect.x -= SPEED_X_ENEMY[0]
        elif self.count < 60:
            self.rect.x += SPEED_X_ENEMY[0]
        else:
            self.rect.x += SPEED_X_ENEMY[0]
            self.count = 0

    def move_chasing(self, spaceship): # movimiento del enemigo 2
        if spaceship > self.rect.x:
            self.rect.x += SPEED_X_ENEMY[1]
        else:
            self.rect.x -= SPEED_X_ENEMY[1]

    def control_out_screen(self): # evitar que salga de la pantalla 
        if self.rect.x > SCREEN_WIDTH - IMAGE_SIZE[0]:
            self.rect.x = 0
        elif self.rect.x < 0:
            self.rect.x = SCREEN_WIDTH - IMAGE_SIZE[0]

    def respawn_enemy(self): # reaparecer el enemigo si este no muere
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y = 0
            if self.type_enemy <= 2:
                self.rect.x = random.randint(0,SCREEN_WIDTH)