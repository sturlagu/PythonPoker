import os
import pygame


class Card:
    base_path = os.path.dirname(__file__)
    WIDTH = 125
    HEIGHT = 175

    def __init__(self, card, card_state):
        if card_state == "show":
            self.card = card
            self.image = pygame.transform.scale(pygame.image.load(os.path.join(self.base_path + "/images/cards/", self.card + ".png")), (self.WIDTH, self.HEIGHT))
        elif card_state == "hide":
            self.card = card
            self.image = pygame.transform.scale(pygame.image.load(os.path.join(self.base_path + "/images/cards/", "purple_back.png")), (self.WIDTH, self.HEIGHT))
        else:
            self.image = pygame.transform.scale(pygame.image.load(os.path.join(self.base_path + "/images/cards/", "purple_back.png")), (self.WIDTH, self.HEIGHT))

    def draw(self, pos, screen):
        screen.blit(self.image, (pos[0], pos[1]))

    def new_card(self, card, card_state):
        if card_state == "show":
            self.card = card
            self.image = pygame.transform.scale(pygame.image.load(os.path.join(self.base_path + "/images/cards/", self.card + ".png")), (self.WIDTH, self.HEIGHT))
        elif card_state == "hide":
            self.card = card
            self.image = pygame.transform.scale(pygame.image.load(os.path.join(self.base_path + "/images/cards/", "purple_back.png")), (self.WIDTH, self.HEIGHT))

    def show_card(self):
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(self.base_path + "/images/cards/", self.card + ".png")), (self.WIDTH, self.HEIGHT))

    def hide_card(self):
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(self.base_path + "/images/cards/", "purple_back.png")), (self.WIDTH, self.HEIGHT))

