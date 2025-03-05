import pygame

pygame.init()

WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Figura z 3 kształtów")


BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

circle_center = (WIDTH // 2, HEIGHT // 2)
circle_radius = 120

square_size = 100
square_pos = (circle_center[0] - square_size // 2, circle_center[1] - square_size // 2)

triangle_points = [
    (circle_center[0] - square_size // 2, circle_center[1] - square_size // 2), 
    (circle_center[0] + square_size // 2, circle_center[1] - square_size // 2),  
    (circle_center[0], circle_center[1] - circle_radius)  
]


running = True
while running:
    screen.fill(WHITE)

    pygame.draw.circle(screen, BLACK, circle_center, circle_radius)

    pygame.draw.rect(screen, YELLOW, (square_pos[0], square_pos[1], square_size, square_size))

    pygame.draw.polygon(screen, BLACK, triangle_points)

    pygame.display.flip()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
