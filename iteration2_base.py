from pygame.locals import *
import pygame
# import time

grid_size = 44

class Player:
  # Change these attributes:
  x = 40
  y = 40
  speed = 1

  # Change this:
  def __str__(self):
    return str("Current coordinates: {}, {}".format(self.x, self.y))

  #
  # Add an __init__ constructor here
  #

  #
  # Add update()
  # 
  
  # Change this to account for  the  step function:
  def move(self, x, y):                 
    self.x = self.x + (self.speed * x)
    self.y = self.y + (self.speed * y)

# Setting up the class for our games
class App:
  windowWidth = 800
  windowHeight = 600
  player = 0

  # Our app's constructor
  def __init__(self):
    self._running = False
    self._player_image = None 
    self._display = None
    self.player = Player()      # Pass argument here

  def on_execute(self):
    pygame.init() 

    self._display = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)

    pygame.display.set_caption('Hacksu Snake! 🐍')

    self._player_image = pygame.image.load("mario.png").convert()

    self._player_image = pygame.transform.scale(self._player_image, (grid_size, grid_size))

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

      # time.sleep(0.3)

    # This will ONLY be called once  that while loop is exited. 
    self.on_cleanup()
 
  def on_loop(self):
    #  Call player.update()
    pass
 
  # Rendering out specific images
  def on_render(self):
    self._display.fill((0,0,0))

    # Replace this with the for loop renderer:
    self._display.blit(self._player_image,(self.player.x,self.player.y))

    pygame.display.flip() # "Flips" the graphics to our new specifications
 
  def on_cleanup(self):
    pygame.quit()

# This is what starts the whole game:
if __name__ == "__main__" :
  theApp = App()
  theApp.on_execute()