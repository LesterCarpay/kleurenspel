# import pygame module in this program
import os.path
from functools import reduce
import pygame
import random


def get_random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def get_average_color(colors):
    average_rgba = reduce(lambda x, y: x.lerp(y, 0.5), colors)
    return average_rgba


def get_radius(i, frame_rate=30):
    return int(1000/(i//frame_rate + 20))


def get_position_color(image, coordinate, radius, average=True):
    if average:
        perimeter_coordinates = [(coordinate[0] + radius, coordinate[1]),
                                 (coordinate[0] - radius, coordinate[1]),
                                 (coordinate[0], coordinate[1] + radius),
                                 (coordinate[0], coordinate[1] - radius)]

        perimeter_colors = []
        for pc in perimeter_coordinates:
            try:
                perimeter_colors.append(image.get_at(pc))
            except IndexError:
                continue
        average_color_perimeter = get_average_color(perimeter_colors)
        average_color = image.get_at(coordinate).lerp(average_color_perimeter, 0.5)
        return average_color
    return image.get_at(coordinate)



def get_image():
    return pygame.image.load(os.path.join("images", "girl_with_pearl_earring.jpg"))

# activate the pygame library
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# create the display surface object
# (x, y) is the height and width of pygame window

image = get_image()
win = pygame.display.set_mode(image.get_size())

# set the pygame window name
pygame.display.set_caption("Een scherm")
win.blit(image, (0, 0))

done = False
clock = pygame.time.Clock()

# infinite loop
col = get_random_color()
circle_positions = []
circle_colors = []
mouse_pressed = False

while not done:
    win.fill((250, 250, 250))
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method
    mouse_position = (0, 0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_pressed = False
        elif event.type == pygame.MOUSEMOTION:
            mouse_position = event.pos


    if mouse_pressed:
        circle_positions.append(mouse_position)
        col = get_position_color(image, mouse_position, get_radius(len(circle_positions) - 1))
        circle_colors.append(col)

    for i in range(len(circle_positions)):
        position = circle_positions[i]
        color = circle_colors[i]
        pygame.draw.circle(win, color, position, get_radius(i))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
