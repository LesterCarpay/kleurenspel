from typing import Callable
import pygame


class MenuButton:
    # formatting constants
    button_width = 140
    button_height = 40
    font_name = "Comicsans"
    font_size = 35
    text_color = (255, 255, 255)
    unselected_color = (100, 100, 100)
    selected_color = (170, 170, 170)

    def __init__(self, x, y, text: str, click_function: Callable[[], None]):
        self.rectangle = pygame.Rect(x, y, MenuButton.button_width, MenuButton.button_height)
        font = pygame.font.SysFont(MenuButton.font_name, MenuButton.font_size)
        self.rendered_text = font.render(text, True, MenuButton.text_color)
        self.click_function = click_function

    def get_rectangle(self):
        return self.rectangle

    def get_rendered_text(self):
        return self.rendered_text

    def mouse_is_on_button(self, mouse_position: tuple[int, int]) -> bool:
        return self.rectangle.collidepoint(mouse_position)

    def get_button_color(self, selected: bool):
        if selected:
            return self.selected_color
        else:
            return self.unselected_color

    def get_text_position(self) -> tuple[int, int]:
        return (self.rectangle.x + 0.5 * self.rectangle.width - 0.5 * self.rendered_text.get_width(),
                self.rectangle.top + 0.5 * self.rectangle.height - 0.5 * self.rendered_text.get_height())

    def click(self) -> None:
        self.click_function()
