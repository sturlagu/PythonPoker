import pygame
import os
import random

from BetButton import BetButton
from Button import Button
from Card import Card
from FoldButton import FoldButton
from StayButton import StayButton


class Board:
    WIDTH = 1300
    HEIGHT = 1000
    base_path = os.path.dirname(__file__)
    BG_IMG = pygame.image.load(os.path.join(base_path + "/images/", 'tableBackground.jpg'))

    SPACING = 10
    PLAYER_CARD_ONE_POSITION = (((WIDTH / 2) - Card.WIDTH - SPACING), (HEIGHT - Card.HEIGHT - SPACING * 5))
    PLAYER_CARD_TWO_POSITION = (((WIDTH / 2) + SPACING), (HEIGHT - Card.HEIGHT - SPACING * 5))
    BOT_CARD_ONE_POSITION = (((WIDTH / 2) - Card.WIDTH - SPACING), (SPACING * 5))
    BOT_CARD_TWO_POSITION = (((WIDTH / 2) + SPACING), (SPACING * 5))
    CARD_DECK_POSITION = ((SPACING * 5), (HEIGHT / 2) - (Card.HEIGHT / 2))
    DEALT_CARD_ONE_POSITION = (((WIDTH / 2) - Card.WIDTH * 2.5 - SPACING * 2), (HEIGHT / 2) - (Card.HEIGHT / 2))
    DEALT_CARD_TWO_POSITION = (((WIDTH / 2) - Card.WIDTH * 1.5 - SPACING), (HEIGHT / 2) - (Card.HEIGHT / 2))
    DEALT_CARD_THREE_POSITION = ((WIDTH / 2) - (Card.WIDTH / 2), (HEIGHT / 2) - (Card.HEIGHT / 2))
    DEALT_CARD_FOUR_POSITION = (((WIDTH / 2) + Card.WIDTH - SPACING * 2), (HEIGHT / 2) - (Card.HEIGHT / 2))
    DEALT_CARD_FIVE_POSITION = (((WIDTH / 2) + Card.WIDTH * 2 + SPACING * 2), (HEIGHT / 2) - (Card.HEIGHT / 2))
    BET_BUTTON_POSITION = (((WIDTH / 2) + Card.WIDTH + Button.WIDTH), (HEIGHT - Button.HEIGHT * 2))
    STAY_BUTTON_POSITION = (((WIDTH / 2) + Card.WIDTH + Button.WIDTH * 2 + SPACING), (HEIGHT - Button.HEIGHT * 2))
    FOLD_BUTTON_POSITION = (((WIDTH / 2) + Card.WIDTH + Button.WIDTH * 3 + SPACING * 2), (HEIGHT - Button.HEIGHT * 2))

    CARDS = ["2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD", "AD",
             "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH", "AH",
             "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC", "AC",
             "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS", "AS"]

    def __init__(self):
        pygame.display.set_caption("Texas Hold'em Poker")
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.player_card_one = Card(self.pick_random_card(), "show")
        self.player_card_two = Card(self.pick_random_card(), "show")
        self.bot_card_one = Card(self.pick_random_card(), "hide")
        self.bot_card_two = Card(self.pick_random_card(), "hide")
        self.card_deck = Card("", "")
        self.dealt_card_one = Card(self.pick_random_card(), "hide")
        self.dealt_card_two = Card(self.pick_random_card(), "hide")
        self.dealt_card_three = Card(self.pick_random_card(), "hide")
        self.dealt_card_four = Card(self.pick_random_card(), "hide")
        self.dealt_card_five = Card(self.pick_random_card(), "hide")
        self.bet_button = BetButton(self.BET_BUTTON_POSITION)
        self.stay_button = StayButton(self.STAY_BUTTON_POSITION)
        self.fold_button = FoldButton(self.FOLD_BUTTON_POSITION)

    def draw_board(self):
        self.screen.blit(self.BG_IMG, (0, 0))
        self.draw_player_cards()
        self.draw_dealt_cards()
        self.draw_card_deck()
        self.draw_buttons()

    def draw_dealt_cards(self):
        self.dealt_card_one.draw(self.DEALT_CARD_ONE_POSITION, self.screen)
        self.dealt_card_two.draw(self.DEALT_CARD_TWO_POSITION, self.screen)
        self.dealt_card_three.draw(self.DEALT_CARD_THREE_POSITION, self.screen)
        self.dealt_card_four.draw(self.DEALT_CARD_FOUR_POSITION, self.screen)
        self.dealt_card_five.draw(self.DEALT_CARD_FIVE_POSITION, self.screen)

    def draw_player_cards(self):
        self.player_card_one.draw(self.PLAYER_CARD_ONE_POSITION, self.screen)
        self.player_card_two.draw(self.PLAYER_CARD_TWO_POSITION, self.screen)
        self.bot_card_one.draw(self.BOT_CARD_ONE_POSITION, self.screen)
        self.bot_card_two.draw(self.BOT_CARD_TWO_POSITION, self.screen)

    def draw_card_deck(self):
        self.card_deck.draw(self.CARD_DECK_POSITION, self.screen)
        self.card_deck.draw((self.CARD_DECK_POSITION[0] - 5, self.CARD_DECK_POSITION[1]), self.screen)
        self.card_deck.draw((self.CARD_DECK_POSITION[0] - 10, self.CARD_DECK_POSITION[1]), self.screen)
        self.card_deck.draw((self.CARD_DECK_POSITION[0] - 15, self.CARD_DECK_POSITION[1]), self.screen)
        self.card_deck.draw((self.CARD_DECK_POSITION[0] - 20, self.CARD_DECK_POSITION[1]), self.screen)
        self.card_deck.draw((self.CARD_DECK_POSITION[0] - 25, self.CARD_DECK_POSITION[1]), self.screen)

    def draw_buttons(self):
        self.bet_button.draw(self.screen)
        self.stay_button.draw(self.screen)
        self.fold_button.draw(self.screen)

    def show_dealt_cards(self, game_round):
        if game_round == 1:
            self.dealt_card_one.show_card()
            self.dealt_card_two.show_card()
            self.dealt_card_three.show_card()
        elif game_round == 2:
            self.dealt_card_four.show_card()
        elif game_round == 3:
            self.dealt_card_five.show_card()
        elif game_round == 4:
            self.bot_card_one.show_card()
            self.bot_card_two.show_card()

    def check_mouse_input(self, pos):
        if self.stay_button.click_button(pos):
            return self.stay_button.click_button(pos)
        elif self.fold_button.click_button(pos):
            self.reset_cards()
            return self.fold_button.click_button(pos)

    def pick_random_card(self):
        card = random.choice(self.CARDS)
        self.CARDS.remove(card)
        return card

    def reset_cards(self):
        self.reset_card_list()
        self.player_card_one.new_card(self.pick_random_card(), "show")
        self.player_card_two.new_card(self.pick_random_card(), "show")
        self.bot_card_one.new_card(self.pick_random_card(), "hide")
        self.bot_card_two.new_card(self.pick_random_card(), "hide")
        self.dealt_card_one.new_card(self.pick_random_card(), "hide")
        self.dealt_card_two.new_card(self.pick_random_card(), "hide")
        self.dealt_card_three.new_card(self.pick_random_card(), "hide")
        self.dealt_card_four.new_card(self.pick_random_card(), "hide")
        self.dealt_card_five.new_card(self.pick_random_card(), "hide")

    def reset_card_list(self):
        self.CARDS = ["2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD", "AD",
                      "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH", "AH",
                      "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC", "AC",
                      "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS", "AS"]
