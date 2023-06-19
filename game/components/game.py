import pygame
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, ALL_SPRITES, GROUP_SPACESHIP
from game.components.spaceship import SpaceShip
from game.components.game_control import Game_control

# Game tiene un "Spaceship" - Por lo general esto es iniciliazar un objeto Spaceship en el __init__
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False  # variable de control para salir del ciclo
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.reset_button = False
        self.attempt = 1
        # Game tiene un "Spaceship" y un "Enemy"
        self.spaceship = SpaceShip()
        GROUP_SPACESHIP.add(self.spaceship)
        ALL_SPRITES.add(self.spaceship)
        self.game_control = Game_control()

    def reset(self):
        if self.reset_button:
            ALL_SPRITES.empty()
            self.spaceship = SpaceShip()
            GROUP_SPACESHIP.add(self.spaceship)
            ALL_SPRITES.add(self.spaceship)
            self.game_control = Game_control()
            self.reset_button = False
            self.attempt += 1

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        # while self.playing == True
        while self.playing: # Mientras el atributo playing (self.playing) sea true "repito"
            self.handle_events()
            self.update()
            self.draw()
            self.reset()

        pygame.display.quit()
        pygame.quit()

    def handle_events(self):
        self.spaceship.move() # capturar eventos del teclado para el movimiento
        # control de colisiones
        self.game_control.control_collide_enemy()
        self.game_control.control_collide_player(self.screen)
        self.reset_button = self.game_control.press_reset_button()
        # Para un "event" (es un elemento) en la lista (secuencia) que me retorna el metodo get()
        for event in pygame.event.get():
            # si el "event" type es igual a pygame.QUIT entonces cambiamos playing a False
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        self.spaceship.update()
        self.game_control.update(self.spaceship.rect.x)
        self.game_control.add_enemys_time()
        self.spaceship.kill() if self.game_control.count_lives == 0 else None

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.game_control.count_kills_attempt(self.screen, self.attempt)
        self.game_control.draw_lives(self.screen)
        # dibujamos todos los objetos o sprites en pantalla
        ALL_SPRITES.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed