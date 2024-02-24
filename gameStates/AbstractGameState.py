from abc import ABC, abstractmethod

from GameSettings import GameSettings


class AbstractGameState(ABC):

    def __init__(self, game_settings: GameSettings):
        self.game_settings = game_settings

    @abstractmethod
    def activate(self):
        """
        Activates the game state, returns the next game state to be activated.
        """
        pass
