from game.components.enemy import Enemy
import random, pygame
from game.utils.constants import SCREEN_WIDTH, ALL_SPRITES, GROUP_ENEMYS, GROUP_SPACESHIP, GROUP_BULLETS

class Control:
    def __init__(self):
        self.count = 300
        self.enemys = []
        self.timer = 0

    def add_enemys_time(self): # agrega 4 enemygos cada cierto tiempo
        self.count += 1
        if self.count > 300:
            self.count = 0
            for i in range(4):
                enemy = Enemy(random.randint(0, SCREEN_WIDTH))
                self.enemys.append(enemy)
                GROUP_ENEMYS.add(enemy)
                ALL_SPRITES.add(enemy)

    def update(self, rect_x):
        for enemy in self.enemys:
            enemy.update(rect_x)

    def control_collide_enemy(self): # controla las coliciones entre balas y enemigos
        collide_enemy = pygame.sprite.groupcollide(GROUP_BULLETS, GROUP_ENEMYS, True, True)
        self.respawn_enemy() if collide_enemy else None
        
    def control_collide_player(self): # controla las coliciones entre el jugardor y los enemigos
        collide_player = pygame.sprite.groupcollide(GROUP_ENEMYS, GROUP_SPACESHIP, True, True)
        return False if collide_player else True

    def respawn_enemy(self): # crea un enemigo nuevo
        enemy = Enemy(random.randint(0, SCREEN_WIDTH))
        self.enemys.append(enemy)
        GROUP_ENEMYS.add(enemy)
        ALL_SPRITES.add(enemy)

    def count_time(self, flag): # cuenta el tiempo jugado
        self.timer += 1
        None if flag else print(f'Tiempo jugado: {self.timer/30}')
