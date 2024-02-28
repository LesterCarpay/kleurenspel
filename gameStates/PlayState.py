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
        self.user_input = ""

    def looping_function(self, events) -> bool:
        self.screen.fill((250, 250, 250))
        self.manage_mouse_press(events)
        self.draw_new_circle(pygame.mouse.get_pos())
        self.render_circles()
        self.update_user_input(events)
        self.render_answer_field()

        return True

    def manage_mouse_press(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_pressed = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.mouse_pressed = False

    def draw_new_circle(self, mouse_position):
        if self.mouse_pressed:
            self.circle_positions.append(mouse_position)
            color = self.template_image.get_circle_color(mouse_position,
                                                         radius=self.calculate_radius(len(self.circle_positions) - 1))
            self.circle_colors.append(color)

    def render_circles(self):
        for i in range(len(self.circle_positions)):
            position = self.circle_positions[i]
            color = self.circle_colors[i]
            pygame.draw.circle(self.screen, color, position, self.calculate_radius(i))

    def update_user_input(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.user_input = self.user_input[:-1]
                else:
                    new_character = event.unicode
                    if len(self.user_input) < 20 and (new_character.isalnum() or new_character == " "):
                        self.user_input += event.unicode

    def render_answer_field(self):
        input_font = pygame.font.SysFont("Comicsans", 32)
        text_color = (0, 0, 0, 1)
        placeholder_color = (105, 105, 105)
        placeholder_text = "Type your answer"
        if self.user_input == "":
            rendered_text = input_font.render(placeholder_text, True, placeholder_color)
        else:
            rendered_text = input_font.render(self.user_input, True, text_color)
        text_location = (self.screen.get_width() / 10, self.screen.get_height() * 9/10 - rendered_text.get_height())

        margin_size = 3
        background_rectangle = pygame.Rect(text_location[0] - margin_size,
                                           text_location[1],
                                           rendered_text.get_width() + 2*margin_size,
                                           rendered_text.get_height())
        pygame.draw.rect(self.screen, (250, 250, 250), background_rectangle)
        self.screen.blit(rendered_text, text_location)
