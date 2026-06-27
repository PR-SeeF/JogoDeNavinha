#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Const import WINDOW_WIDTH, WINDOW_HEIGHT, MENU_OPTION, ENTITY_HEALTH, EVENT_ENEMY, ENEMY_CLOCK, \
    ENTITY_POSITION
from code.Controls import Controls
from code.Menu import Menu
from code.Level import Level
import pygame

from code.Score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))

    def run(self):
        player_score: list[int] = [0, 0]
        player_health: list[int] = [300, 300]
        while True:
            controls = Controls(self.window)
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()
            enemy_clock = ENEMY_CLOCK

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.window, 'Level1', menu_return, player_score, player_health)
                level_return = level.run(player_score, player_health, enemy_clock)
                if level_return:
                    enemy_clock = ENEMY_CLOCK - 500
                    level = Level(self.window, 'Level2', menu_return, player_score, player_health)
                    level_return = level.run(player_score, player_health, enemy_clock)
                    if level_return:
                        score.save_score(menu_return, player_score)
            elif menu_return == MENU_OPTION[3]:
                controls.show_controls()
                pass
            elif menu_return == MENU_OPTION[4]:
                score.show_score()
                pass


            elif menu_return == MENU_OPTION[5]:
                pygame.quit()
                quit()
