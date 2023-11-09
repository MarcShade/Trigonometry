import pygame
import math
import numpy

pygame.init()

WIDTH = 1200
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
angle = 33
clock = pygame.time.Clock()
Δt = clock.tick(144)

def gettan(angle):
    radians = angle*(math.pi/180)
    tanrad = math.tan(radians)
    return tanrad

def getsin(angle):
    radians = angle*(math.pi/180)
    sinrad = math.sin(radians)
    return sinrad

def getcos(angle):
    radians = angle*(math.pi/180)
    cosrad = math.cos(radians)
    return cosrad

def draw_dashed_line(surf, color, start_pos, end_pos, width=1, dash_length=10):
    x1, y1 = start_pos
    x2, y2 = end_pos
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

    cos = getcos(angle)
    sin = getsin(angle)
    tan = gettan(angle)

    screen.fill("white")
    angleline = pygame.draw.line(screen, "black", (WIDTH/2, HEIGHT/2), (WIDTH/2 + 325*cos, HEIGHT/2 + 325*(-sin)), 2)
    cosline = draw_dashed_line(screen, "darkblue", (int(WIDTH/2 + 325*cos), int(HEIGHT/2)), (int(WIDTH/2 + 325*cos), int(HEIGHT/2 + 325*(-sin))))
    sinline = draw_dashed_line(screen, "darkred", (int(WIDTH/2), int(HEIGHT/2 + 325*(-sin))), (int(WIDTH/2 + 325*cos), int(HEIGHT/2 + 325*(-sin))))
    tanline = pygame.draw.line(screen, "darkgreen", (WIDTH / 2 + 325, 0), (WIDTH / 2 + 325, HEIGHT), 2)
    x_axis = pygame.draw.line(screen, "black", (0, HEIGHT/2), (WIDTH, HEIGHT/2))
    y_axis = pygame.draw.line(screen, "black", (WIDTH/2, 0), (WIDTH/2, HEIGHT))
    unitcircle = pygame.draw.circle(screen, "black", (WIDTH/2, HEIGHT/2), 326, 2)
    angle += 0.01*Δt
    pygame.display.update()

def run():
    running = True
    while running:
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                quit()
run()        