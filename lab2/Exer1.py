import pygame
import math

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("9-kąt Transformacje")

YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

NUM_SIDES = 9 
RADIUS = 150
CENTER = (WIDTH // 2, HEIGHT // 2)

# Transformacje: (x, y, kąt, skala_x, skala_y, skew_x, skew_y)
TRANSFORMATIONS = {
    pygame.K_1: (CENTER[0], CENTER[1], 0, 0.5, 0.5, 0, 0), 
    pygame.K_2: (CENTER[0], CENTER[1], 45, 1, 1, 0, 0),  
    pygame.K_3: (CENTER[0], CENTER[1], 180, 0.5, 0.75, 0, 0),  # Obrót o 180 stopni + spłaszczenie w poziomie
    pygame.K_4: (CENTER[0], CENTER[1], -30, 1, 1, 0.3, 0),  # Przekrzywienie w trapez
    pygame.K_5: (CENTER[0], 50, 0, 1, 0.5, 0, 0),  # Spłaszczenie w pionie i przeniesienie na górę
    pygame.K_6: (CENTER[0], CENTER[1], 90, 1, 1, 0, 0.3),  # Przekrzywienie w trapez + obrót o 90 stopni
    pygame.K_7: (CENTER[0], CENTER[1], 90, 1, 1, 0, 0),  
    pygame.K_8: (CENTER[0] - 100, CENTER[1] + 100, -45, 1, 1, 0, 0), 
    pygame.K_9: (WIDTH - 100, CENTER[1], 180, 1, 1, 0.3, 0)  # Przekrzywienie + obrót 180° + przesunięcie na prawo
}

# Aktualne parametry
current_transform = (CENTER[0], CENTER[1], 0, 1, 1, 0, 0)

def draw_polygon(x, y, angle, scale_x, scale_y, skew_x, skew_y):
    points = []
    for i in range(NUM_SIDES):
        theta = (2 * math.pi * i / NUM_SIDES) + math.radians(angle)
        px = x + int(RADIUS * scale_x * math.cos(theta))
        py = y + int(RADIUS * scale_y * math.sin(theta))
        
        # Przekrzywienie (skew)
        px += int((py - y) * skew_x)  # Skew w osi X
        py += int((px - x) * skew_y)  # Skew w osi Y
        
        points.append((px, py))
    
    pygame.draw.polygon(screen, BLUE, points)

def main():
    global current_transform
    running = True
    while running:
        screen.fill(YELLOW)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in TRANSFORMATIONS:
                    current_transform = TRANSFORMATIONS[event.key]
        
        # Rysowanie 9-kąta
        draw_polygon(*current_transform)
        
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
