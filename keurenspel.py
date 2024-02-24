# import pygame module in this program
import pygame

from templateimage import TemplateImage

frame_rate = 60


def get_radius_function(starting_radius=150, curve_factor=5, frame_rate=frame_rate):
    """
    Generates a function to use for the radius calculation, based on entered parameters.
    :param starting_radius: the radius the circle should have at the start
    :param curve_factor: determines how fast the radius shrinks, lower curve_factor -> faster shrinking, should be > 0.
    :param frame_rate: the frame rate of the game
    :return: a function that accepts only i, the index of the circle whose radius needs to be calculated
    """
    if curve_factor <= 0:
        raise ValueError("curve_factor should be > 0")
    return lambda i: int(starting_radius*frame_rate*curve_factor/(i+frame_rate*curve_factor))


def play_game():
    pygame.init()
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
    get_radius = get_radius_function()

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


def main():
    play_game()


if __name__== "__main__":
    main()
