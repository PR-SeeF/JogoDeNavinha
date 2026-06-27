

import pygame
from pygame import Surface, KEYDOWN, K_ESCAPE, Rect
from pygame.font import Font

from code.Const import COLOR_CIAN, SCORE_POSITION, WINDOW_WIDTH, COLOR_ORANGE


class Controls:

    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        pass

    def show_controls(self):
        pygame.mixer.music.load('./asset/Score.mp3')
        pygame.mixer.music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(40, 'CONTROLS', COLOR_ORANGE, text_pos= (WINDOW_WIDTH  / 2, 50))
        self.score_text(15, 'Player1                        Player2', COLOR_ORANGE, text_pos=(WINDOW_WIDTH / 2, 90))
        self.score_text(15, 'MOVE                           MOVE', COLOR_ORANGE, text_pos=(WINDOW_WIDTH / 2, 110))
        self.score_text(15, '↑ - TOP                        W - TOP', COLOR_ORANGE, text_pos=(WINDOW_WIDTH / 2, 130))
        self.score_text(15, '→ - RIGHT                      D - RIGHT', COLOR_ORANGE, text_pos=(WINDOW_WIDTH / 2, 150))
        self.score_text(15, '← - LEFT                       A - LEFT', COLOR_ORANGE, text_pos=(WINDOW_WIDTH / 2, 170))
        self.score_text(15, '↓ - DOWN                       ↓ - DOWN', COLOR_ORANGE, text_pos=(WINDOW_WIDTH / 2, 190))
        self.score_text(15, 'RCTRL - SHOOT                  LCTRL - SHOOT', COLOR_ORANGE, text_pos=(WINDOW_WIDTH / 2, 210))

        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
                if event.type == pygame.QUIT:
                    pygame.quit()  # close window
                    quit()  # end pygame
            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="ARIAL", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_pos)
        self.window.blit(source=text_surf, dest=text_rect)

