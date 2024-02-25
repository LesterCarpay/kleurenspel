import pygame

from gameStates.MenuButton import MenuButton


class Menu:

    def __init__(self):
        self.buttons: list[MenuButton] = []
        self.background_image = pygame.image.load("menu_background.png")
        self.background_image = pygame.transform.scale(self.background_image,
                                                       size=tuple(
                                                           0.5 * dim for dim in self.background_image.get_size()))

    def add_button(self, button: MenuButton):
        self.buttons.append(button)

    def handle_mouse_click(self, mouse_position):
        for button in self.buttons:
            if button.mouse_is_on_button(mouse_position):
                button.click()

    def render(self, screen, mouse_position):
        screen.blit(self.background_image, (0, 0))

        for button in self.buttons:
            selected = button.mouse_is_on_button(mouse_position)
            color = button.get_button_color(selected=selected)
            pygame.draw.rect(screen, color, button.get_rectangle())
            screen.blit(button.get_rendered_text(), button.get_text_position())
