from abc import ABC, abstractmethod

from GameSettings import GameSettings
from typing import Optional


class AbstractGameState(ABC):

    def __init__(self, game_settings: GameSettings):
        self.game_settings = game_settings

    @abstractmethod
    def activate(self) -> Optional['AbstractGameState']:
        """
        Activates the game state, returns the next game state to be activated.
        """
        pass
