import pygame

from GameSettings import GameSettings
from gameStates.AbstractGameState import AbstractGameState
from gameStates.MenuButton import MenuButton
from gameStates.PlayState import PlayState
from templateimage import TemplateImage

from gameStates.Menu import Menu


class StartMenuState(AbstractGameState):

    def __init__(self, game_settings: GameSettings):
        super().__init__(game_settings)

        start_menu = Menu()
        screen = pygame.display.set_mode(start_menu.background_image.get_size())
        play_button = MenuButton(x=screen.get_width() / 2 - 0.5 * MenuButton.button_width,
                                 y=screen.get_height() * (1 / 3) - 0.5 * MenuButton.button_height,
                                 text="play",
                                 click_function=lambda: StartMenuState.start_game(self))
        quit_button = MenuButton(x=screen.get_width() / 2 - 0.5 * MenuButton.button_width,
                                 y=screen.get_height() * (2 / 3) - 0.5 * MenuButton.button_height,
                                 text="quit",
                                 click_function=pygame.quit)

        start_menu.add_button(play_button)
        start_menu.add_button(quit_button)

        self.start_menu = start_menu
        self.screen = screen

    def looping_function(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.start_menu.handle_mouse_click(pygame.mouse.get_pos())

        self.start_menu.render(self.screen, pygame.mouse.get_pos())
        pygame.display.update()

    def start_game(self):
        image = TemplateImage.get_random_image()
        PlayState(game_settings=self.game_settings, template_image=image).activate()
