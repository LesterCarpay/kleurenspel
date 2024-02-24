# import pygame module in this program
import pygame

from GameSettings import GameSettings
from gameStates.PlayState import PlayState
from templateimage import TemplateImage


def main():
    pygame.init()
    pygame.display.set_caption("Kleurenspel")
    image = TemplateImage.get_random_image()
    settings = GameSettings()
    PlayState(game_settings=settings, template_image=image).activate()
    pygame.quit()


if __name__ == "__main__":
    main()
