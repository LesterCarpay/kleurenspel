import pygame

from GameSettings import GameSettings
from gameStates.AbstractGameState import AbstractGameState
from gameStates.CategorySelectionState import CategorySelectionState
from gameStates.MenuButton import MenuButton


class StartMenuState(AbstractGameState):

    def __init__(self, game_settings: GameSettings):
        super().__init__(game_settings)
        self.background_image = pygame.image.load("menu_background.png")
        self.background_image = pygame.transform.scale(self.background_image,
                                                  size=tuple(
                                                      0.5 * dim for dim in self.background_image.get_size()))
        screen = pygame.display.set_mode(self.background_image.get_size())
        select_category_function = CategorySelectionState(game_settings=self.game_settings).activate
        play_button = MenuButton(x=screen.get_width() / 2 - 0.5 * MenuButton.button_width,
                                 y=screen.get_height() * (1 / 3) - 0.5 * MenuButton.button_height,
                                 text="play",
                                 click_function=select_category_function)
        quit_button = MenuButton(x=screen.get_width() / 2 - 0.5 * MenuButton.button_width,
                                 y=screen.get_height() * (2 / 3) - 0.5 * MenuButton.button_height,
                                 text="quit",
                                 click_function=pygame.quit)
        self.buttons.append(play_button)
        self.buttons.append(quit_button)
        self.screen = screen

    def looping_function(self, events):
        self.screen.blit(self.background_image, (0, 0))
        pygame.display.update()

