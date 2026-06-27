#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Enemy import Enemy
from code.Player import Player
from code.Background import Background
from code.Const import WINDOW_WIDTH, WINDOW_HEIGHT, ENTITY_POSITION


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WINDOW_WIDTH, 0)))
                return list_bg
            case 'Level2Bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level2Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level2Bg{i}', (WINDOW_WIDTH, 0)))
                return list_bg
            case 'Level3Bg':
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(f'Level3Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level3Bg{i}', (WINDOW_WIDTH, 0)))
                return list_bg

            case 'Player1':
                return Player(name='Player1',
                              position=(ENTITY_POSITION['Player1'][0], ENTITY_POSITION['Player1'][1] - 30))
            case 'Player2':
                return Player(name='Player2',
                              position=(ENTITY_POSITION['Player2'][0], ENTITY_POSITION['Player2'][1] + 30))
            case 'Enemy1':
                return Enemy(name='Enemy1', position=(WINDOW_WIDTH + 5, random.randint(0, WINDOW_HEIGHT - 50)))
            case 'Enemy2':
                return Enemy(name='Enemy2', position=(WINDOW_WIDTH + 5, random.randint(0, WINDOW_HEIGHT - 50)))
