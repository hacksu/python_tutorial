from pygame.locals import *
import pygame
import time
# from random import randint

grid_size = 44

#
# Add  Apple class
#

class Player:
  x = []
  y = []
  speed = 1
  step = grid_size
  
  x_direction = 1  
  y_direction = 0   
  length = 3

  def __init__(self, length):
    self.length = length
    for i in range(0,length):
      self.x.append(0)
      self.y.append(0)

  def update(self):
    for i in range(self.length-1,0,-1):
      self.x[i] = self.x[i-1]
      self.y[i] = self.y[i-1]

    self.x[0] = self.x[0] + (self.step * self.x_direction)
    self.y[0] = self.y[0] + (self.step * self.y_direction)


  def __str__(self):
    return "self.x[" + str(self.x[0]) + "] = self.x[" + str(self.y[0]) + "]"

  def move(self, x, y):    
    self.x_direction = x
    self.y_direction = y

class App:
  windowWidth = 800
  windowHeight = 600
  player = 0

  def __init__(self):
    self._running = False
    self._player_image = None   

    # Declare apple image here

    self._display = None  
    self.player = Player(3) 

    # Instatiate apple

  def on_execute(self):
    pygame.init() 

    self._display = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)

    pygame.display.set_caption('Hacksu Snake! 🐍')

    self._player_image = pygame.image.load("mario.png").convert()
    self._player_image = pygame.transform.scale(self._player_image, (grid_size, grid_size))

    # Set up the apple image here


    self._running =  True

    while( self._running ):
      pygame.event.pump()
      keys = pygame.key.get_pressed() 

      if (keys[K_RIGHT]):
        self.player.move(1, 0)
      elif (keys[K_LEFT]):
        self.player.move(-1, 0)
      if (keys[K_DOWN]):
        self.player.move(0, 1)
      elif (keys[K_UP]):
        self.player.move(0, -1)
      
      if (keys[K_SPACE]):
        print(self.player)

      if (keys[K_ESCAPE]):
        self._running = False

      self.on_loop()
      self.on_render()

      time.sleep (0.3)

    self.on_cleanup()
 
  def on_loop(self):
    self.player.update()

    #
    # Add apple collisions here
    #

    #
    # Add snake collisions here
    #

    pass
 
  #
  # Add collision function here
  #

  def on_render(self):
    self._display.fill((0,0,0))
    
    for i in range(0,self.player.length):
      self._display.blit(self._player_image, (self.player.x[i], self.player.y[i])) 

    # Draw the apple here

    pygame.display.flip() 
 
  def on_cleanup(self):
    pygame.quit()

if __name__ == "__main__" :
  theApp = App()
  theApp.on_execute()