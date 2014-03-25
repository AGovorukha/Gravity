#!/bin/env python

import random
import pygame, math
from pygame import *
from math import *

WIN_WIDTH = 800
WIN_HEIGHT = 640
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
SPACE_COLOR = "#000022"
G = 6.6

class Planet(sprite.Sprite):

   def __init__(self, rad, mas, x, y, vx, vy, ax=0, ay=0, planet_color="green"):
      sprite.Sprite.__init__(self)
      self.width = rad
      self.height = rad
      self.color = planet_color
      self.x = x
      self.y = y
      self.vx = vx
      self.vy = vy
      self.ax = ax
      self.ay = ay
      self.radius = rad
      self.mass = mas

   def move(self, planet):
      self.r = sqrt((self.x - planet.x)**2 + (self.y - planet.y)**2)

      self.ax =  planet.mass * (planet.x - self.x) / self.r**3
      self.ay =  planet.mass * (planet.y - self.y) / self.r**3

      #New spped based on accel
      self.vx += self.ax
      self.vy += self.ay

      #New pos based on speed
      self.x += self.vx
      self.y += self.vy


   def drawing(self, scrn):
      pygame.draw.circle(scrn, Color(self.color), (self.x, self.y), self.radius)


def main():
    #PyGame init
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Solar Mechanics v0.1")

    #Space init
    bg = Surface((WIN_WIDTH,WIN_HEIGHT))
    bg.fill(Color(SPACE_COLOR))

    #Timer init
    timer = pygame.time.Clock()

    #Stars init
    for count in range(1, 100):
       star_X = random.randrange(10, 780)
       star_Y = random.randrange(10, 630)
       draw.circle(bg, Color('white'), (star_X, star_Y), 0.5)

    #Planet init
    Sun = Planet(20, 3330, 400, 320, 0.2, 0.2, 0, 0, 'yellow')
    Earth = Planet(5, 2, 210, 320, 0, 4.25, 0, 0, 'blue')
    Planet2 = Planet(3, 1, 150, 320, 0, 3.7, 0, 0, 'white')
    Planet3 = Planet(3, 40, 230, 320, 0, 4.5, 0, 0, 'red')
    Planet4 = Planet(15, 4, 130, 50, 0, 3, 0, 0, 'green')

    done = False
    while not done:
        timer.tick(50)
        for e in pygame.event.get():
            if e.type == QUIT:
                done = True
                break

        Earth.move(Sun)
        Sun.move(Earth)
        Planet2.move(Sun)
        Planet3.move(Sun)
        Planet4.move(Sun)

        screen.blit(bg, (0, 0))
        Sun.drawing(screen)
        Earth.drawing(screen)
        Planet2.drawing(screen)
        Planet3.drawing(screen)
        Planet4.drawing(screen)
        pygame.display.update()

    #Farewell
    print (":-)")

if __name__ == "__main__":
    main()

