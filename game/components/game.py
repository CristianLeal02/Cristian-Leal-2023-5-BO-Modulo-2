import pygame
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, \
    ALL_SPRITES, GROUP_SPACESHIP, GROUP_BULLETS, GROUP_BULLETS_ENEMYS, GROUP_ENEMYS

from game.components.spaceship import SpaceShip
from game.components.enemy import Enemy
from game.components.enemy_control import Enemy_control

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

        # Game tiene un "Spaceship" y un "Enemy"
        self.spaceship = SpaceShip()
        GROUP_SPACESHIP.add(self.spaceship)
        ALL_SPRITES.add(self.spaceship)
        self.enemy_control = Enemy_control()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True

        # while self.playing == True
        while self.playing: # Mientras el atributo playing (self.playing) sea true "repito"
            self.handle_events()
            self.update()
            self.draw()
        else:
            print("Something ocurred to quit the game!!!")
        pygame.display.quit()
        pygame.quit()

    def handle_events(self):
        # Para un "event" (es un elemento) en la lista (secuencia) que me retorna el metodo get()
        for event in pygame.event.get():
            # si el "event" type es igual a pygame.QUIT entonces cambiamos playing a False
            if event.type == pygame.QUIT:
                self.playing = False

        self.enemy_control.add_enemys()

    def update(self):
        # pass
        self.spaceship.update()
        self.enemy_control.update(self.spaceship.rect.x)
        pygame.sprite.groupcollide(GROUP_BULLETS, GROUP_ENEMYS, True, True)
        pygame.sprite.groupcollide(GROUP_BULLETS_ENEMYS, GROUP_SPACESHIP, True, True)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()

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
