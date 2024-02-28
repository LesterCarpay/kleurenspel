import pygame

from GameSettings import GameSettings
from gameStates.AbstractGameState import AbstractGameState
from gameStates.MenuButton import MenuButton
from gameStates.PlayState import PlayState
from TemplateImage import TemplateImage, ImageCategory
from functools import partial


class CategorySelectionState(AbstractGameState):

    def __init__(self, game_settings: GameSettings):
        super().__init__(game_settings)
        self.background_image = pygame.image.load("menu_background.png")
        self.background_image = pygame.transform.scale(self.background_image,
                                                       size=tuple(
                                                           0.5 * dim for dim in self.background_image.get_size()))
        screen = pygame.display.set_mode(self.background_image.get_size())
        for i, category in enumerate(ImageCategory):
            n_categories = len(ImageCategory)
            play_function = partial(CategorySelectionState.start_game, self, category)
            category_button = MenuButton(x=screen.get_width() / 2 - 0.5 * MenuButton.button_width,
                                         y=screen.get_height() * (
                                                     (i + 1) / (n_categories + 1)) - 0.5 * MenuButton.button_height,
                                         text=category.name,
                                         click_function=play_function)
            self.buttons.append(category_button)

        self.screen = screen

    def looping_function(self, events):
        self.screen.blit(self.background_image, (0, 0))
        pygame.display.update()

    def start_game(self, category):
        image = TemplateImage.get_random_image(category)
        PlayState(game_settings=self.game_settings, template_image=image).activate()
