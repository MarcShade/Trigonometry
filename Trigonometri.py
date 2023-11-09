import pygame
import math
import numpy

pygame.init()

WIDTH = 1920
HEIGHT = 1040
ORIGO = (WIDTH/2, HEIGHT/2)
radius = 450

screen = pygame.display.set_mode((WIDTH, HEIGHT))
angle = 0
clock = pygame.time.Clock()

def draw_dashed_line(surf, color, start_pos, end_pos, width=3, dash_length=8):
    x1, y1 = start_pos
    x2, y2 = end_pos
    x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
    dl = dash_length

    if (x1 == x2):
        ycoords = [y for y in range(y1, y2, dl if y1 < y2 else -dl)]
        xcoords = [x1] * len(ycoords)
    elif (y1 == y2):
        xcoords = [x for x in range(x1, x2, dl if x1 < x2 else -dl)]
        ycoords = [y1] * len(xcoords)
    else:
        a = abs(x2 - x1)
        b = abs(y2 - y1)
        c = round(math.sqrt(a**2 + b**2))
        dx = dl * a / c
        dy = dl * b / c

        xcoords = [x for x in numpy.arange(x1, x2, dx if x1 < x2 else -dx)]
        ycoords = [y for y in numpy.arange(y1, y2, dy if y1 < y2 else -dy)]

    next_coords = list(zip(xcoords[1::2], ycoords[1::2]))
    last_coords = list(zip(xcoords[0::2], ycoords[0::2]))
    for (x1, y1), (x2, y2) in zip(next_coords, last_coords):
        start = (round(x1), round(y1))
        end = (round(x2), round(y2))
        pygame.draw.line(surf, color, start, end, width)

def draw():
    global angle
    cos = math.cos(math.radians(angle))
    sin = math.sin(math.radians(angle))
    tan = math.tan(math.radians(angle))

    screen.fill("white")
    dashed_cosline = draw_dashed_line(screen, "blue", (int(ORIGO[0] + radius*cos), int(ORIGO[1])), (int(ORIGO[0] + radius*cos), int(ORIGO[1] + radius*(-sin))))
    dashed_sinline = draw_dashed_line(screen, "red", (int(ORIGO[0]), int(ORIGO[1] + radius*(-sin))), (int(ORIGO[0] + radius*cos), int(ORIGO[1] + radius*(-sin))))
    dashed_tanline = draw_dashed_line(screen, "chartreuse4", ORIGO, (ORIGO[0] + radius, numpy.clip(ORIGO[1] - radius*tan, -20000, 20000)))
    
    angleline = pygame.draw.line(screen, "black", (ORIGO[0], ORIGO[1]), (ORIGO[0] + radius*cos, ORIGO[1] + radius*(-sin)), 3)   
    
    x_axis = pygame.draw.line(screen, "black", (0, ORIGO[1]), (WIDTH, ORIGO[1]))
    y_axis = pygame.draw.line(screen, "black", (ORIGO[0], 0), (ORIGO[0], HEIGHT))

    cosline = pygame.draw.line(screen, "blue", (ORIGO[0], ORIGO[1]), (ORIGO[0] + radius*cos, ORIGO[1]), 3)
    sinline = pygame.draw.line(screen, "red", (ORIGO[0], ORIGO[1]), (ORIGO[0], ORIGO[1] + radius*(-sin)), 3)
    tanline = pygame.draw.line(screen, "chartreuse4", (ORIGO[0] + radius, 0), (ORIGO[0] + radius, HEIGHT), 3)
    
    unitcircle = pygame.draw.circle(screen, "black", (ORIGO[0], ORIGO[1]), radius, 3)
    
    angle += 0.3
    pygame.display.update()
    clock.tick(144)

def run():
    running = True
    while running:
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                quit()
run()        