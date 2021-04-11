import pygame, sys

from Game import Game
from Draw import Draw



def main_loop():
    pygame.init()
    pygame.display.set_caption('Tic Tac Toe')
    icon = pygame.image.load('img/ico.png')
    pygame.display.set_icon(icon)
    screen = pygame.display.set_mode((500,300))

    draw = Draw(screen)
    game = Game()

    round = 0
    run = True
    while run:
        for event in pygame.event.get():
            draw.draw_bord()

            if event.type == pygame.QUIT:
                run = False


            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    x,y = mouse_pos


                    centerPosX, centerPosY = game.mouse_center(x, y)

                    if game.can_move(centerPosX, centerPosY) == True:

                        round = game.round_handler(round, draw,centerPosX, centerPosY)
                        if round>=4:
                            if game.win_condition(draw) != 0:
                                break

                        if round > 8:
                            draw.no_one_win()
                            break



main_loop()