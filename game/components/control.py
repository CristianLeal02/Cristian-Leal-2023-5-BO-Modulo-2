from game.components.enemy import Enemy
import random, pygame
from game.utils.constants import SCREEN_WIDTH, ALL_SPRITES, GROUP_ENEMYS, GROUP_SPACESHIP,  \
    GROUP_BULLETS, GROUP_BULLETS_ENEMYS, ALL_SPRITES, GROUP_BULLETS_ENEMYS
from game.components.items import Game_over

class Control:
    def __init__(self):
        self.count = 0
        self.enemys = []
        self.timer = 0
        self.add_enemys_init()
        self.end = False
        self.group_game_over = pygame.sprite.Group()
        self.playing = True

    def add_enemys_init(self):
        for i in range(3):
            enemy = Enemy(random.randint(0, SCREEN_WIDTH))
            self.enemys.append(enemy)
            GROUP_ENEMYS.add(enemy)
            ALL_SPRITES.add(enemy)

    def add_enemys_time(self): # agrega enemigos cada cierto tiempo
        self.count += 1
        if self.count > 300 and self.playing:
            self.count = 0
            enemy = Enemy(random.randint(0, SCREEN_WIDTH))
            self.enemys.append(enemy)
            GROUP_ENEMYS.add(enemy)
            ALL_SPRITES.add(enemy)

    def update(self, rect_x):
        for enemy in self.enemys:
            if self.playing:
                enemy.update(rect_x)
            else:
                enemy.kill()

    def control_collide_enemy(self): # controla las coliciones entre balas y enemigos
        collide_enemy = pygame.sprite.groupcollide(GROUP_BULLETS, GROUP_ENEMYS, True, True)
        self.respawn_enemy() if collide_enemy else None
        
    def control_collide_player(self, screen): # controla las coliciones entre el jugardor, las balas y los enemigos
        collide_player = pygame.sprite.groupcollide(GROUP_ENEMYS, GROUP_SPACESHIP, True, True)
        collide_player_2 = pygame.sprite.groupcollide(GROUP_BULLETS_ENEMYS, GROUP_SPACESHIP, True, True)
        self.game_over(screen) if (collide_player or collide_player_2) else True

    def respawn_enemy(self): # crea un enemigo nuevo
        if self.playing:
            enemy = Enemy(random.randint(0, SCREEN_WIDTH))
            self.enemys.append(enemy)
            GROUP_ENEMYS.add(enemy)
            ALL_SPRITES.add(enemy)

    def count_time(self, flag): # cuenta el tiempo jugado
        self.timer += 1
        None if flag else print(f'Tiempo jugado: {self.timer/30}')

    def game_over(self, screen):
        game_over = Game_over()
        ALL_SPRITES.remove()
        GROUP_BULLETS_ENEMYS.remove()
        self.group_game_over.add(game_over)
        ALL_SPRITES.add(game_over)
        self.playing = False
        return True

