import random, pygame
from game.components.enemy import Enemy
from game.components.game_over import Game_over
from game.components.lives import Lives
from game.components.reset_button import Reset_button
from game.utils.constants import SCREEN_WIDTH, ALL_SPRITES, GROUP_ENEMYS, GROUP_SPACESHIP, \
    GROUP_BULLETS, GROUP_BULLETS_ENEMYS, ALL_SPRITES, GROUP_BULLETS_ENEMYS, FONT_STYLE

class Game_control:
    def __init__(self):
        self.count_updates = 0
        self.enemys = []
        self.timer = 0
        self.add_enemys_init()
        self.playing = True
        self.count_kill = 0
        self.count_lives = 5
        self.reset_button = Reset_button(273)
        self.font = pygame.font.SysFont(FONT_STYLE, 30)
        self.flag_timer = False

    def add_enemys_init(self): # agrega enemigos al iniciar
        for i in range(3):
            enemy = Enemy(random.randint(0, SCREEN_WIDTH))
            self.enemys.append(enemy)
            GROUP_ENEMYS.add(enemy)
            ALL_SPRITES.add(enemy)

    def add_enemys_time(self): # agrega enemigos cada cierto tiempo
        self.count_updates += 1
        if (self.count_updates % 300 == 0) and self.playing:
            enemy = Enemy(random.randint(0, SCREEN_WIDTH))
            self.enemys.append(enemy)
            GROUP_ENEMYS.add(enemy)
            ALL_SPRITES.add(enemy)

    def update(self, rect_x):
        self.press_reset_button()
        for enemy in self.enemys:
            if self.playing:
                enemy.update(rect_x)
            else:
                enemy.kill()

    def control_collide_enemy(self): # controla las coliciones entre balas y enemigos
        collide_enemy = pygame.sprite.groupcollide(GROUP_BULLETS, GROUP_ENEMYS, True, True)
        if collide_enemy:
            self.count_kill += 1
            self.respawn_enemy()
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

    def game_over(self, screen): # pantalla de game over
        if self.count_lives == 0:
            game_over = Game_over(screen)
            ALL_SPRITES.add(game_over, self.reset_button)
            self.playing = False
            self.flag_timer = True

    def count_kills_attempt(self, screen, attempt): # textos contadores de kills e intentos o reinicios
        text_kill = self.font.render(f"Kills: {self.count_kill}", True, (200, 0, 0))
        text_attempt = self.font.render(f"Attempt: {attempt}", True, (0, 177, 237))
        self.draw_text(text_attempt, 60, 15, screen)
        self.draw_text(text_kill, 45, 38, screen)
        if self.flag_timer:
            timer = self.font.render(f"Tiempo jugado: {self.timer//30} segundos", True, (0, 177, 237))
            self.draw_text(timer, 550, 325, screen)
        else:
            self.timer += 1

    def draw_text(self, text, rect_x, rect_y, screen): # dibuja los textos
        text_rect = text.get_rect()
        text_rect.center = (rect_x, rect_y)
        screen.blit(text, text_rect)

    def draw_lives(self, screen): # dibuja las vidas
        rect_x = 1080
        for i in range(self.count_lives):
            live = Lives(rect_x)
            screen.blit(live.image, live.rect)
            rect_x -= 30

    def press_reset_button(self): # funcion del boton de reinicio
        if pygame.mouse.get_pressed()[0]:
            if self.reset_button.rect.collidepoint(pygame.mouse.get_pos()):
                pygame.time.delay(100)
                return True