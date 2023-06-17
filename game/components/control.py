from game.components.enemy import Enemy
import random, pygame
from game.utils.constants import SCREEN_WIDTH, ALL_SPRITES, GROUP_ENEMYS, GROUP_SPACESHIP,  \
    GROUP_BULLETS, GROUP_BULLETS_ENEMYS, ALL_SPRITES, GROUP_BULLETS_ENEMYS, BG, FONT_STYLE
from game.components.game_over import Game_over

class Control:
    def __init__(self):
        self.count_updates = 0
        self.enemys = []
        self.timer = 0
        self.add_enemys_init()
        self.playing = True
        self.flag = True
        self.count_kill = 0
        self.count_lives = 5

    def add_enemys_init(self):
        for i in range(3):
            enemy = Enemy(random.randint(0, SCREEN_WIDTH))
            self.enemys.append(enemy)
            GROUP_ENEMYS.add(enemy)
            ALL_SPRITES.add(enemy)

    def add_enemys_time(self): # agrega enemigos cada cierto tiempo
        self.count_updates += 1
        if self.count_updates > 300 and self.playing:
            self.count_updates = 0
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
        if collide_enemy:
            self.respawn_enemy()
            self.count_kill += 1
        else: None
        
    def control_collide_player(self, screen): # controla las coliciones entre el jugardor, las balas y los enemigos
        collide_player = pygame.sprite.groupcollide(GROUP_ENEMYS, GROUP_SPACESHIP, True, False)
        collide_player_2 = pygame.sprite.groupcollide(GROUP_BULLETS_ENEMYS, GROUP_SPACESHIP, True, False)
        if collide_player:
            self.count_lives -= 1 
            self.respawn_enemy()
            self.game_over(screen)
        elif collide_player_2:
            self.count_lives -= 1 
            self.game_over(screen)

    def respawn_enemy(self): # crea un enemigo nuevo
        if self.playing:
            enemy = Enemy(random.randint(0, SCREEN_WIDTH))
            self.enemys.append(enemy)
            GROUP_ENEMYS.add(enemy)
            ALL_SPRITES.add(enemy)

    def count_time(self): # cuenta el tiempo jugado
        self.timer += 1
        if not self.flag:
            print(f'Tiempo jugado: {self.timer/30} segundos')
            self.flag = True

    def game_over(self, screen):
        if self.count_lives == 0:
            game_over = Game_over(screen)
            ALL_SPRITES.add(game_over)
            self.playing = False
            self.flag = False
            self.count_time()

    def count_kills(self, screen):
        font = pygame.font.SysFont(FONT_STYLE, 30)
        text_kill = font.render(f"Kills: {self.count_kill}", True, (0, 255, 255))
        text_kill_rect = text_kill.get_rect()
        text_kill_rect.center = (50, 20)
        screen.blit(text_kill, text_kill_rect)