from dataclasses import dataclass
from typing import Callable


@dataclass
class GameSettings:
    """Class defining the game settings.
        Attributes:
            frame_rate (int): The frame rate at which the game runs.
            starting_radius (int): The radius of the drawing circle at the start of the game.
            curve_factor (float): Defines how fast the circle shrinks, smaller means faster shrinking.
                                  Value should be > 0.
        """
    frame_rate = 60
    starting_radius = 150
    curve_factor = 3.0

    def __post_init__(self):
        if self.curve_factor <= 0:
            raise ValueError("curve_factor should be > 0")

    def get_radius_function(self) -> Callable[[int], int]:
        """
        Generates a function to use for the radius calculation, based on the game settings.
        """
        return lambda i: int(self.starting_radius * self.frame_rate * self.curve_factor /
                             (i + self.frame_rate * self.curve_factor))
