import pygame, sys

class Game:

    def __init__(self):
        self.squares = [(50, 50, "empty"), (150, 50, "empty"), (250, 50, "empty"),
                        (50,150,"empty"), (150,150,"empty"), (250,150,"empty"),
                        (50,250,"empty"), (150,250,"empty"), (250,250,"empty")]
    def mouse_center(self, x, y):

        for rectangle in self.squares:
            recMidX, recMidY, free = rectangle

            if abs(recMidX - x) <= 50 and abs(recMidY - y) <= 50:

                centerPosX = recMidX
                centerPosY = recMidY

                return centerPosX, centerPosY

    def round_handler(self, round, draw, x, y):

        round += 1
        for i in range (9):
            tupleX, tupleY, is_busy = self.squares[i]
            if tupleX == x and tupleY == y:
                pos = i
                break

        if round % 2 == 0:
            player = "Kółko"
            draw.draw_round_text(player)
            self.squares[pos] = (x, y, "x")
            draw.draw_x(x, y)
        else:
            player = "Krzyżyk"
            draw.draw_round_text(player)
            self.squares[pos] = (x, y, "o")
            draw.draw_circle(x, y)
        return round

    def can_move(self, x, y):

        for i in range(9):
            tupleX, tupleY, is_busy = self.squares[i]

            if tupleX == x and tupleY == y:
                if is_busy == "empty":
                    return True
                else:
                    return False


    def win_condition(self, draw):

        wining_combinations = (

        (self.squares[0], self.squares[4], self.squares[8]),

        (self.squares[0], self.squares[1], self.squares[2]),
        (self.squares[3], self.squares[4], self.squares[5]),
        (self.squares[6], self.squares[7], self.squares[8]),

        (self.squares[0], self.squares[3], self.squares[6]),
        (self.squares[1], self.squares[4], self.squares[7]),
        (self.squares[2], self.squares[5], self.squares[8])
        )

        for i in range(7):
            sq_1, sq_2, sq_3 = wining_combinations[i]

            x1, y1, str1 = sq_1
            x2, y2, str2 = sq_2
            x3, y3, str3 = sq_3

            # print(f"Combination:{i}   string1: {str1}, string2: {str2}, string1: {str3}")

            if (str1 == str2 and str2 == str3 and str1 != "empty"):

                deltaX = abs(x3 - x1)
                deltaY = abs(y3 - y1)

                draw.draw_winer_line(x1 - deltaX, y1 - deltaY, x3 + deltaX, y3 + deltaY)
                if str1 == "x":
                    print("Wygrana X")
                    draw.set_can_draw(False)
                    draw.draw_winer_text(win="krzyżyk!")
                    draw.draw_play_again()
                    return "x_win"
                else:
                    print ("Wygrana O!")
                    draw.set_can_draw(False)
                    draw.draw_winer_text(win="kółko!")
                    draw.draw_play_again()
                    return "o_win"

        return 0

    def get_pos(self):
        return self.squares
