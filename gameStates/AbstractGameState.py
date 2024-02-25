from abc import ABC, abstractmethod

from GameSettings import GameSettings
import pygame

from gameStates.MenuButton import MenuButton


class AbstractGameState(ABC):

    def __init__(self, game_settings: GameSettings):
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

            try:
                self.looping_function(events)
            except QuitGameException:
                pygame.quit()
                return

            pygame.display.flip()
            self.clock.tick(self.game_settings.frame_rate)


class QuitGameException(Exception):
    pass
