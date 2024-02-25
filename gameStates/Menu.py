import pygame

from gameStates.MenuButton import MenuButton


class Menu:

    def __init__(self):
        self.background_image = pygame.image.load("menu_background.png")
        self.background_image = pygame.transform.scale(self.background_image,
                                                       size=tuple(
                                                           0.5 * dim for dim in self.background_image.get_size()))
        self.buttons = []

    def add_button(self, button: MenuButton):
        self.buttons.append(button)

