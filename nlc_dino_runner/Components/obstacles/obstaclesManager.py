import pygame.time
import random

from nlc_dino_runner.Components.obstacles import cactus
from nlc_dino_runner.Components.obstacles.bird import Bird
from nlc_dino_runner.Components.obstacles.cactus import Cactus
from nlc_dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD


class ObstaclesManager:
    def __init__(self):
        self.obstacles_list = []

    def update(self, game):
        if len(self.obstacles_list) == 0:
            cactus = Cactus(random.choice([SMALL_CACTUS, LARGE_CACTUS]))
            bird = Bird(BIRD)
            obstacle = random.choice([cactus, bird])
            self.obstacles_list.append(obstacle)

        for obstacle in self.obstacles_list:
            obstacle.update(game.game_speed, self.obstacles_list)
            if game.player.dino_rect.colliderect(obstacle.rect):  # Rect1.colliderect(Rect2)
                if game.player.shield:
                    self.obstacles_list.remove(obstacle)
                elif game.lives_manager.number_of_lives == 1:
                    pygame.time.delay(1000)
                    game.playing = False
                    game.death_count += 1
                    break
                else:
                    game.lives_manager.reduce_live()
                    self.obstacles_list.remove(obstacle)

    def draw(self, screen):
        for obstacle in self.obstacles_list:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles_list = []

#Commit "Clase 4 - Colisiones"
