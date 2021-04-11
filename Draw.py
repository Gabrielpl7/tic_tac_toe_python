import pygame, sys


class Draw:
    def __init__(self, screen):
        self.screen = screen
        self.can_draw = True

    def draw_bord(self):
        rows = 2
        x = 0
        y = 0
        a = 100

        for i in range(3):
            x = 0
            for i in range(3):
                pygame.draw.rect(self.screen, (200, 200, 200), pygame.Rect(x, y, a, a), 2)
                x += 100
            y += 100
        pygame.display.flip()

    def draw_circle(self, x, y):
        if self.can_draw == True:
            pygame.draw.circle(self.screen, (200,200,200), (x,y), 30, 5)


    def draw_x(self, x, y):

        if self.can_draw == True:
            pygame.draw.line(self.screen, (255, 0, 0), (x, y), (x + 25, y + 25), 5)
            pygame.draw.line(self.screen, (255, 0, 0), (x, y), (x - 25, y - 25), 5)
            pygame.draw.line(self.screen, (255, 0, 0), (x, y), (x + 25, y - 25), 5)
            pygame.draw.line(self.screen, (255, 0, 0), (x, y), (x - 25, y + 25), 5)

    def draw_winer_line(self, start_x, start_y, end_x, end_y):
        pygame.draw.line(self.screen, (255, 0, 0), (start_x, start_y), (end_x, end_y), 5)

    def draw_round_text(self, player):
        pygame.draw.rect(self.screen, (255, 0, 0), (340, 50, 120, 50))

        font = pygame.font.SysFont(None, 24)
        img = font.render(f'Ruch: {player}', True, (255, 255, 255))
        self.screen.blit(img, (345, 70))

    def draw_winer_text(self, win):

        font = pygame.font.SysFont(None, 24)
        img = font.render(f'Wygrywa {win}', True, (255, 255, 255))
        self.screen.blit(img, (340, 220))

    def no_one_win(self):

        font = pygame.font.SysFont(None, 24)
        img = font.render('Remis!', True, (255, 255, 255))
        self.screen.blit(img, (365, 220))

    def draw_play_again(self):
        pass

    def get_can_draw(self):
        return self.can_draw

    def set_can_draw(self, can_draw):
        self.can_draw = can_draw


