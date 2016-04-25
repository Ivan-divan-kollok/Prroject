import pygame
import random

pygame.init()

class vector():

    def __init__(self, x = [0]):
        self.x = x

    def __add__(self, b):
        c = vector(range(0,len(self.x)))
        for i in range(0, len(self.x)):
            c.x[i] = self.x[i] + b.x[i]
        return c

    def __sub__(self, b):
        d = vector(range(0,len(self.x)))
        for i in range(0, len(self.x)):
            d.x[i] = self.x[i] - b.x[i]
        return d

    def scalar(self, b):
        c = 0
        for i in range(0,len(self.x)):
            c = c + self.x[i] * b.x[i]
        return c


size = width, height = 600, 600
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)


v = vector([0, 0])
r = vector([100+random.random()*100, 0])

prev_t = pygame.time.get_ticks()
ar = pygame.PixelArray(screen)

i=1
rad=6
k=0.4


while True:
    delta = clock.tick(50) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    g=400;
    r.x[0] += v.x[0] * delta
    r.x[1] += v.x[1] * delta-0.5*g*delta*delta
    v.x[1] +=0.5*g*delta
    i+=1
    j=1


    while  (r.x[1]>200)and(r.x[1]<204)and(r.x[0]>100)and(r.x[0]<450):
        v.x[1] = 50
        v.x[1] = 0
        r.x[0] +=v.x[0] * delta







    if i < 117:
        if r.x[0] < rad:
            if v.x[0] < 0:
                v.x[0] = -v.x[0]
                r.x[0] = rad
        if r.x[1] < rad:
            if v.x[1] < 0:
                v.x[1] = -v.x[1]
                r.x[1] = -rad
        if r.x[0] > 600-rad:
            if v.x[0] > 0:
                v.x[0] = -v.x[0]
                r.x[0] = 600-rad

        if r.x[1] > 600-rad:
            if v.x[1] > 0:
                v.x[1] = -k*v.x[1]
                r.x[1] = 600-rad

    if i >= 117:
        if r.x[0] < rad:
            if v.x[0] < 0:
                v.x[0] = -v.x[0]
                r.x[0] = rad
        if r.x[1] < rad:
            if v.x[1] < 0:
                v.x[1] = -v.x[1]
                r.x[1] = -rad
        if r.x[0] > 600-rad:
            if v.x[0] > 0:
                v.x[0] = -v.x[0]
                r.x[0] = 600-rad

        if r.x[1] > 600-rad:
            if v.x[1] > 0:
                v.x[1] = -k*v.x[1]
                r.x[1] = 600-rad
        #v.x[0] = 5000*(random.random()*10*(-1)**i)/(i)








    screen.fill((0, 0, 0))
    col = 255
    pygame.draw.circle(screen, (col/99, col, col), (int(r.x[0]), int(r.x[1])), rad)
    pygame.display.flip()
