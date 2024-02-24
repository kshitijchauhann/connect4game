# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 800))

# text written above the Pygame window
pygame.display.set_caption("Connect4")

# load image as icon
icon = pygame.image.load("/home/kshitijc/Downloads/C.png")

# set image as icon
pygame.display.set_icon(icon)

# function to draw circles
def draw_circles(num_circles, num_lines, surface, color, start_x, start_y, radius, space):
    for line in range(num_lines):
        center_x = start_x
        center_y = start_y + (2 * radius + space) * line
        for i in range(num_circles):
            pygame.draw.circle(surface, color, (center_x, center_y), radius)
            center_x += radius * 2 + space
        

running = True
while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # background color
    screen.fill("black")

    draw_circles(10, 10, screen, "silver", 100, 100, 30, 6)
   
    # flip() the display to put your work on screenreen
    pygame.display.flip()

pygame.quit()
