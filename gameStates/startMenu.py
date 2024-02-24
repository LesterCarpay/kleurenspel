import pygame

from gameStates.AbstractGameState import AbstractGameState
from gameStates.PlayState import PlayState
from templateimage import TemplateImage


class StartMenuState(AbstractGameState):

    def activate(self):
        pygame.init()
        pygame.display.set_caption("Kleurenspel")

        background_image = pygame.image.load("menu_background.png")
        background_image = pygame.transform.scale(background_image,
                                                  size=tuple(0.5 * dim for dim in background_image.get_size()))
        screen = pygame.display.set_mode(background_image.get_size())

        # white color
        color = (255, 255, 255)

        # light shade of the button
        color_light = (170, 170, 170)

        # dark shade of the button
        color_dark = (100, 100, 100)

        # defining a font
        smallfont = pygame.font.SysFont('Corbel', 35)

        button_width = 140
        button_height = 40
        play_rectangle = pygame.Rect(screen.get_width() / 2 - 0.5 * button_width,
                                     screen.get_height() * (1 / 3) - 0.5 * button_height,
                                     button_width, button_height)
        quit_rectangle = pygame.Rect(screen.get_width() / 2 - 0.5 * button_width,
                                     screen.get_height() * (2 / 3) - 0.5 * button_height,
                                     button_width, button_height)

        play_text = smallfont.render('play', True, color)
        quit_text = smallfont.render('quit', True, color)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if quit_rectangle.collidepoint(event.pos):
                        pygame.quit()
                        return
                    elif play_rectangle.collidepoint(event.pos):
                        self.start_game()
                        pygame.quit()

            screen.blit(background_image, (0, 0))
            mouse = pygame.mouse.get_pos()

            if quit_rectangle.collidepoint(mouse):
                pygame.draw.rect(screen, color_light, quit_rectangle)
            else:
                pygame.draw.rect(screen, color_dark, quit_rectangle)

            if play_rectangle.collidepoint(mouse):
                pygame.draw.rect(screen, color_light, play_rectangle)
            else:
                pygame.draw.rect(screen, color_dark, play_rectangle)

            # superimposing the text onto our button
            screen.blit(play_text, (play_rectangle.left + 0.5 * play_rectangle.width - 0.5 * play_text.get_width(),
                                    play_rectangle.top + 0.5 * play_rectangle.height - 0.5 * play_text.get_height()))
            screen.blit(quit_text, (quit_rectangle.left + 0.5 * quit_rectangle.width - 0.5 * quit_text.get_width(),
                                    quit_rectangle.top + 0.5 * quit_rectangle.height - 0.5 * quit_text.get_height()))

            # updates the frames of the game
            pygame.display.update()

    def start_game(self):
        image = TemplateImage.get_random_image()
        PlayState(game_settings=self.game_settings, template_image=image).activate()
