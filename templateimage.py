import os
from functools import reduce

import pygame


class TemplateImage:

    width = 500
    max_height = 500
    image_folder_name = "images"

    def __init__(self, file_path: str):
        self.image = TemplateImage._load_image(file_path)

    def get_image(self):
        return self.image

    def get_size(self):
        return self.image.get_size()

    @staticmethod
    def _load_image(file_path: str):
        return pygame.image.load(os.path.join(TemplateImage.image_folder_name, file_path))

    @classmethod
    def get_random_image(cls):
        return cls("statue_of_liberty.jpg")

    @staticmethod
    def get_average_color(colors):
        average_rgba = reduce(lambda x, y: x.lerp(y, 0.5), colors)
        return average_rgba

    def get_circle_color(self, coordinate, radius, average=True):
        if average:
            perimeter_coordinates = [(coordinate[0] + radius, coordinate[1]),
                                     (coordinate[0] - radius, coordinate[1]),
                                     (coordinate[0], coordinate[1] + radius),
                                     (coordinate[0], coordinate[1] - radius)]

            perimeter_colors = []
            for pc in perimeter_coordinates:
                try:
                    perimeter_colors.append(self.image.get_at(pc))
                except IndexError:
                    continue
            average_color_perimeter = TemplateImage.get_average_color(perimeter_colors)
            average_color = self.image.get_at(coordinate).lerp(average_color_perimeter, 0.5)
            return average_color
        return self.image.get_at(coordinate)