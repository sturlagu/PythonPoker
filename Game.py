import pygame
from Board import Board


class Game:
    GAME_ROUND = 0

    def __init__(self, board):
        self.board = board

    def main(self):
        run = True
        while run:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    run = False
                elif events.type == pygame.MOUSEBUTTONDOWN:
                    value = self.board.check_mouse_input(pygame.mouse.get_pos())
                    if isinstance(value, int):
                        if value == -1:
                            self.GAME_ROUND = 0
                        else:
                            if self.GAME_ROUND < 5:
                                self.GAME_ROUND = self.GAME_ROUND + value

            self.board.draw_board()
            self.board.show_dealt_cards(self.GAME_ROUND)
            pygame.display.flip()
        pygame.quit()
        quit()


game_board = Board()
game = Game(game_board)
game.main()
