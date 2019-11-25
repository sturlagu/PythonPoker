import os
import pygame


class Button:
    base_path = os.path.dirname(__file__)
    WIDTH = 100
    HEIGHT = 100

    def __init__(self, button, pos, button_value):
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(self.base_path + "/images/", button + ".png")), (self.WIDTH, self.HEIGHT))
        self.x = pos[0]
        self.y = pos[1]
        self.button_value = button_value

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def click_button(self, pos):
        if self.x < pos[0] < (self.x + self.WIDTH) and self.y < pos[1] < (self.y + self.HEIGHT):
            return self.button_value
