import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 800))
color = ["silver"] * 100

# text written above the Pygame window
pygame.display.set_caption("Connect4")

# load image as icon
icon = pygame.image.load("/home/kshitijc/Downloads/C.png")

# set image as icon
pygame.display.set_icon(icon)

# function to draw circles
def draw_circles(num_circles, surface, color, start_x, start_y, radius, space):
    circles = []
    for col in range(num_circles):
        center_x = start_x
        center_y = start_y + (2 * radius + space) * col
        for row in range(num_circles):
            colors = color[col * num_circles + row]
            pygame.draw.circle(surface, colors, (center_x, center_y), radius)
            circles.append((center_x, center_y))
            center_x += radius * 2 + space
    return circles
    
circle_centers = draw_circles(10, screen, color, 100, 100, 30, 6)

running = True
while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                for center_x, center_y in circle_centers:
                    distance_squared = (mouse_x - center_x) ** 2 + (mouse_y - center_y) **2
                    if distance_squared <= 30 ** 2:
                        # Each element in the list corresponds to a circle in the grid, 
                        # and its index represents the position of the circle in the grid.
                        index = circle_centers.index((center_x, center_y))
                        color[index] = "green" if color[index] == "silver" else "silver"


   # background color
    screen.fill("black")

    draw_circles(10, screen, color, 100, 100, 30, 6)

    # display update
    pygame.display.flip()


pygame.quit()
