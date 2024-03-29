import os
import random
from enum import Enum, auto
from functools import reduce

import pygame


class ImageCategory(Enum):
    animals = auto()
    landmarks = auto()
    art = auto()


class TemplateImage:
    width = 800
    max_height = 600
    image_folder_name = "images"

    def __init__(self, file_path: str):
        self.image = TemplateImage._load_image(file_path)
        self.scale_image()

    def get_image(self):
        return self.image

    def get_size(self):
        return self.image.get_size()

    @staticmethod
    def _load_image(file_path: str):
        return pygame.image.load(file_path)

    def scale_image(self):
        current_width, current_height = self.image.get_size()
        factor = TemplateImage.width / current_width
        new_width, new_height = current_width * factor, current_height * factor
        if new_height > TemplateImage.max_height:
            factor = TemplateImage.max_height / current_height
            new_width, new_height = current_width * factor, current_height * factor
        self.image = pygame.transform.scale(self.image, size=(new_width, new_height))

    @classmethod
    def get_random_image(cls, category: ImageCategory):
        category_folder = os.path.join(cls.image_folder_name, category.name)
        images_files = os.listdir(category_folder)
        images_files = [image_file for image_file in images_files if image_file[-4:] == ".jpg"]
        random_file = random.choice(images_files)
        return cls(os.path.join(category_folder, random_file))

    @staticmethod
    def get_average_color(colors):
        average_rgba = reduce(lambda x, y: x.lerp(y, 0.5), colors)
        return average_rgba

    def get_circle_color(self, coordinate, radius, average=False):
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

