import pygame

from GameSettings import GameSettings
from gameStates.AbstractGameState import AbstractGameState
from TemplateImage import TemplateImage


class PlayState(AbstractGameState):

    def __init__(self, game_settings: GameSettings, template_image: TemplateImage):
        super().__init__(game_settings)
        self.screen = pygame.display.set_mode(template_image.get_size())
        self.template_image = template_image
        self.circle_positions = []
        self.circle_colors = []
        self.mouse_pressed = False
        self.calculate_radius = self.game_settings.get_radius_function()

    def looping_function(self, events) -> bool:
        self.screen.fill((250, 250, 250))
        mouse_position = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_pressed = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.mouse_pressed = False

        if self.mouse_pressed:
            self.circle_positions.append(mouse_position)
            color = self.template_image.get_circle_color(mouse_position,
                                                         radius=self.calculate_radius(len(self.circle_positions) - 1))
            self.circle_colors.append(color)

        for i in range(len(self.circle_positions)):
            position = self.circle_positions[i]
            color = self.circle_colors[i]
            pygame.draw.circle(self.screen, color, position, self.calculate_radius(i))
        return True
