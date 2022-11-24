import random

import pygame

size = width, height = 400,300
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption('Шарики')
running = True

circle_radius = 10
circle_color = pygame.Color((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
circle = []
speed = []
screen2 = pygame.Surface(screen.get_size())
while running:
    for event in pygame.event.get():
        screen2 = pygame.Surface(screen.get_size())
        if event.type == pygame.MOUSEBUTTONUP:
            circle.append(list(event.pos))
            speed.append([-1,-1])
    screen2.fill(pygame.Color('black'))
    for i in range(len(circle)):
        for ext in (0,1):
            if circle[i][ext] >= size[ext] - circle_radius or circle[i][ext] <= circle_radius:
                speed[i][ext] = -speed[i][ext]
            circle[i][ext] += speed[i][ext]

        pygame.draw.circle(screen2,circle_color,circle[i], circle_radius,0)

    screen.blit(screen2,(0,0))
    pygame.display.flip()
    clock.tick(30)
pygame.quit()