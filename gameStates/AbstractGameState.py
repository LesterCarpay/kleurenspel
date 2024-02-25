from abc import ABC, abstractmethod

from GameSettings import GameSettings
import pygame

from gameStates.MenuButton import MenuButton


class AbstractGameState(ABC):

    def __init__(self, game_settings: GameSettings):
        self.screen = None
        self.clock = pygame.time.Clock()
        self.game_settings = game_settings
        self.buttons: list[MenuButton] = []
        pygame.init()
        pygame.display.set_caption("Kleurenspel")

    @abstractmethod
    def looping_function(self, events):
        """
        Handles everything that needs to happen repeatedly every frame.
        :return: True if the game should continue, False if it should quit.
        """
        pass

    def activate(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in self.buttons:
                        if button.mouse_is_on_button(pygame.mouse.get_pos()):
                            button.click()
                            return

            self.looping_function(events)

            self.render_buttons()
            pygame.display.flip()
            self.clock.tick(self.game_settings.frame_rate)

    def render_buttons(self):
        for button in self.buttons:
            selected = button.mouse_is_on_button(pygame.mouse.get_pos())
            color = button.get_button_color(selected=selected)
            pygame.draw.rect(self.screen, color, button.get_rectangle())
            self.screen.blit(button.get_rendered_text(), button.get_text_position())
