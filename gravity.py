#!/bin/env python

import random
import pygame, math
from pygame import *
from math import *

WIN_WIDTH = 800
WIN_HEIGHT = 640
PLANET_WIDTH = 20
PLANET_HEIGHT = 20
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
SPACE_COLOR = "#000022"
SUN_COLOR = "yellow"
PLANET_COLOR = "blue"
STAR_COLOR = "red"

#Sun position
X0 = WIN_WIDTH // 2
Y0 = WIN_HEIGHT // 2
#Sun mass
M0 = 333000
#Stop conditions
CRASH_DIST = 10
OUT_DIST = 1000

class Planet(sprite.Sprite):

   def __init__(self, PLANET_WIDTH, PLANET_HEIGHT, X, Y, VX, VY, AX, AY, radius=5, R=0.0, PLANET_COLOR="green"):
      sprite.Sprite.__init__(self)
      self.width = PLANET_WIDTH
      self.height = PLANET_HEIGHT
      self.color = PLANET_COLOR
      self.x = X
      self.y = Y
      self.vx = VX
      self.vy = VY
      self.ax = AX
      self.ay = AY
      self.r = R
      self.radius = radius

   def move(self):
      self.r = sqrt((self.x - X0)**2 + (self.y - Y0)**2)
        
      self.ax = M0 * (X0 - self.x) / self.r**3
      self.ay = M0 * (Y0 - self.y) / self.r**3

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
       draw.circle(bg, Color(STAR_COLOR), (star_X, star_Y), 0.5)
   
    #Planet init
    planet1 = Planet(20, 20, 100, 500, 0.1, 1.5, 0.0, 0.0, 5, 0.0, 'red')
    planet2 = Planet(20, 20, 700, 500, 0.1, 1.5, 0.0, 0.0, 5, 0.0, 'white')
    planet3 = Planet(20, 20, 20, 50, 0.1, 1.5, 0.0, 0.0, 5, 0.0, 'green')
    SUN = Planet(30, 30, 400, 320, 0.1, 1.5, 0.0, 0.0, 10, 0.0, 'yellow')

    done = False
    while not done:
        timer.tick(50)
        for e in pygame.event.get():
            if e.type == QUIT:
                done = True
                break        
        planet1.move()
        planet2.move()
        planet3.move()

        screen.blit(bg, (0, 0))      
        planet1.drawing(screen)
        planet2.drawing(screen)
        planet3.drawing(screen)
        SUN.drawing(screen)
        pygame.display.update()     


    #Farewell
    print (":-)")

if __name__ == "__main__":
    main()
