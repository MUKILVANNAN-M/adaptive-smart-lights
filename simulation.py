import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Smart Adaptive Lights Simulation")

BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
WHITE = (255, 255, 255)

road_y = HEIGHT // 2
lanes = [road_y - 40, road_y + 20]

streetlights = [(150, road_y - 70), (350, road_y - 70),
                (550, road_y - 70), (750, road_y - 70)]

class Vehicle:
    def __init__(self, x, y, speed):
        self.rect = pygame.Rect(x, y, 50, 30)
        self.speed = speed

    def move(self):
        self.rect.x += self.speed
        if self.rect.x > WIDTH:
            self.rect.x = -50

vehicles = [Vehicle(random.randint(-200, WIDTH),
                    random.choice(lanes),
                    random.randint(2, 4)) for _ in range(3)]

light_intensity = {pos: 100 for pos in streetlights}

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(GRAY)
    pygame.draw.rect(screen, BLACK, (0, road_y - 50, WIDTH, 100))

    for vehicle in vehicles:
        vehicle.move()
        pygame.draw.rect(screen, WHITE, vehicle.rect)

    for (x, y) in streetlights:
        min_distance = min(abs(vehicle.rect.x - x) for vehicle in vehicles)

        target_brightness = 255 if min_distance < 100 else 100

        light_intensity[(x, y)] += (target_brightness - light_intensity[(x, y)]) * 0.1

        color = (light_intensity[(x, y)], light_intensity[(x, y)], 0)
        pygame.draw.circle(screen, color, (x, y), 20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(30)

pygame.quit()
