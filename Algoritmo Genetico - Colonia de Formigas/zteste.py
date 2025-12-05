import pygame
import math
import sys

pygame.init()
w, h = 900, 900
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

N = 5
R = 150
r = 30
cx, cy = w//2, h//2

def star_points(angle):
    pts = []
    for i in range(N*2):
        ang = angle + i * math.pi / N
        radius = R if i % 2 == 0 else r
        x = cx + math.cos(ang) * radius
        y = cy + math.sin(ang) * radius
        pts.append((x, y))
    return pts

def rotate_around(p, pivot, ang):
    px, py = p
    ox, oy = pivot
    s, c = math.sin(ang), math.cos(ang)
    px -= ox
    py -= oy
    xnew = px * c - py * s
    ynew = px * s + py * c
    return (xnew + ox, ynew + oy)

def hsv_to_rgb(h, s, v):
    i = int(h*6)
    f = h*6 - i
    p = v*(1-s)
    q = v*(1-f*s)
    t = v*(1-(1-f)*s)
    i = i % 6
    if i==0: r,g,b = v,t,p
    elif i==1: r,g,b = q,v,p
    elif i==2: r,g,b = p,v,t
    elif i==3: r,g,b = p,q,v
    elif i==4: r,g,b = t,p,v
    else: r,g,b = v,p,q
    return int(r*255), int(g*255), int(b*255)

angle = 0

last_print = 0
delay = 100

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    now = pygame.time.get_ticks()
    if now - last_print >= delay:
        pts = star_points(angle)
        pivot = pts[0]
        rotated = [rotate_around(p, pivot, angle*1.5) for p in pts]

        colors = []
        for i in range(len(rotated)):
            hue = ((i / len(rotated)) + angle*0.1) % 1.0
            colors.append(hsv_to_rgb(hue, 1, 1))

        for i in range(len(rotated)):
            p1 = rotated[i]
            p2 = rotated[(i+1)%len(rotated)]
            c = colors[i]
            pygame.draw.line(screen, c, p1, p2, 2)

        last_print = now

    angle += 0.008
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
