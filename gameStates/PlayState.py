import pygame

from GameSettings import GameSettings
from gameStates.AbstractGameState import AbstractGameState
from templateimage import TemplateImage


class PlayState(AbstractGameState):

    def __init__(self, game_settings: GameSettings, template_image: TemplateImage):
        super().__init__(game_settings)
        self.template_image = template_image

    def activate(self):
        """
        Activates the game state, returns the next game state to be activated.
        """
        image = self.template_image
        win = pygame.display.set_mode(image.get_size())

        # set the pygame window name
        clock = pygame.time.Clock()
        circle_positions = []
        circle_colors = []
        mouse_pressed = False
        mouse_position = (0, 0)
        get_radius = self.game_settings.get_radius_function()

        while True:
            win.fill((250, 250, 250))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pressed = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    mouse_pressed = False
                elif event.type == pygame.MOUSEMOTION:
                    mouse_position = event.pos

            if mouse_pressed:
                circle_positions.append(mouse_position)
                col = image.get_circle_color(mouse_position, get_radius(len(circle_positions) - 1))
                circle_colors.append(col)

            for i in range(len(circle_positions)):
                position = circle_positions[i]
                color = circle_colors[i]
                pygame.draw.circle(win, color, position, get_radius(i))
            pygame.display.flip()
            clock.tick(self.game_settings.frame_rate)
