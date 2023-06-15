from game.components.enemy import Enemy
import random, pygame
from game.utils.constants import SCREEN_WIDTH, ALL_SPRITES, GROUP_ENEMYS

class Enemy_control:
    def __init__(self):
        self.count = 300
        self.enemys = []

    def add_enemys(self):
        self.count += 1
        if self.count > 300:
            self.count = 0
            for i in range(5):
                enemy = Enemy(random.randint(0, SCREEN_WIDTH))
                self.enemys.append(enemy)
                GROUP_ENEMYS.add(enemy)
                ALL_SPRITES.add(enemy)


    def update(self, rect_x):
        for enemy in self.enemys:
            enemy.update(rect_x)
