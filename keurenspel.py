# import pygame module in this program
import pygame

from templateimage import TemplateImage

frame_rate = 60


def get_radius(i, frame_rate=frame_rate):
    return int(1000/(i//frame_rate + 20))


# activate the pygame library
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# create the display surface object
# (x, y) is the height and width of pygame window

image = TemplateImage.get_random_image()
win = pygame.display.set_mode(image.get_size())

# set the pygame window name
pygame.display.set_caption("Kleurenspel")

done = False
clock = pygame.time.Clock()
circle_positions = []
circle_colors = []
mouse_pressed = False
mouse_position = (0, 0)

while not done:
    win.fill((250, 250, 250))
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
        col = image.get_circle_color(mouse_position, get_radius(len(circle_positions) - 1))
        circle_colors.append(col)

    for i in range(len(circle_positions)):
        position = circle_positions[i]
        color = circle_colors[i]
        pygame.draw.circle(win, color, position, get_radius(i))
    pygame.display.flip()
    clock.tick(frame_rate)

pygame.quit()
